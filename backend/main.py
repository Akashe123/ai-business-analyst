import os
import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from io import BytesIO

from src.llm.sql_generator import SQLGenerator
from src.llm.insight_generator import InsightGenerator
from src.database.connector import DatabaseConnector
from src.analysis.analyzer import DataAnalyzer

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

sql_gen = SQLGenerator()
insight_gen = InsightGenerator()
db = DatabaseConnector()
analyzer = DataAnalyzer()

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    sql: str
    data: list
    columns: list
    insights: str
    chart_recommendation: str

@app.post("/api/ask", response_model=AskResponse)
async def ask_question(req: AskRequest):
    sql = sql_gen.generate(req.question)
    rows, columns = db.execute(sql)
    summary = analyzer.summarize(rows, columns)
    insights = insight_gen.generate(req.question, summary)
    chart = analyzer.recommend_chart(columns)
    return AskResponse(
        sql=sql,
        data=rows[:100],
        columns=columns,
        insights=insights,
        chart_recommendation=chart
    )

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    """Upload CSV or Excel file — creates a table in your database"""
    
    if not file.filename.endswith(('.csv', '.xls', '.xlsx')):
        raise HTTPException(400, "Only CSV and Excel files are supported")
    
    # Read file into pandas
    content = await file.read()
    try:
        if file.filename.endswith('.csv'):
            df = pd.read_csv(BytesIO(content))
        else:
            df = pd.read_excel(BytesIO(content))
    except Exception as e:
        raise HTTPException(400, f"Could not read file: {str(e)}")
    
    # Clean column names
    df.columns = [c.strip().lower().replace(" ", "_").replace("-", "_") for c in df.columns]
    
    # Create table name from filename
    table_name = file.filename.rsplit(".", 1)[0].lower().replace(" ", "_").replace("-", "_")
    
    # Upload to Neon
    try:
        engine = db.get_engine()
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        row_count = len(df)
    except Exception as e:
        raise HTTPException(500, f"Database error: {str(e)}")
    
    return {
        "message": f"✅ Uploaded '{file.filename}' as table '{table_name}'",
        "table": table_name,
        "rows": row_count,
        "columns": list(df.columns)
    }

@app.get("/api/tables")
async def list_tables():
    """List all tables in the database"""
    return {"tables": db.get_schema()}

@app.get("/api/schema")
async def get_schema():
    tables = db.get_schema()
    return {"tables": tables}

@app.get("/api/health")
async def health():
    return {"status": "ok"}
