import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from sqlalchemy import create_engine

load_dotenv()

class SQLGenerator:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY")
        )
        db_url = os.getenv("DATABASE_URL")
        if db_url:
            engine = create_engine(db_url, connect_args={"sslmode": "require"})
            self.db = SQLDatabase(engine, sample_rows_in_table_info=0)
        else:
            self.db = None

    def generate(self, question: str) -> str:
        if not self.db:
            return "-- No database configured"
        
        # Get the actual table info
        table_info = self.db.get_table_info()
        
        # Build messages directly (fixing the bug)
        messages = [
            ("system", "You are a SQL expert. You ONLY use tables that actually exist in the schema. Never make up tables."),
            ("human", f"""Database Schema (use ONLY these tables):
{table_info}

Business Question: {question}

Write a PostgreSQL query that answers this question using ONLY the tables above.
Return ONLY the SQL code, nothing else.""")
        ]
        
        response = self.llm.invoke(messages)
        
        sql = response.content.strip()
        if sql.startswith("```sql"):
            sql = sql[6:]
        elif sql.startswith("```"):
            sql = sql[3:]
        if sql.endswith("```"):
            sql = sql[:-3]
        return sql.strip()
