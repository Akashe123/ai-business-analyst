import os
from sqlalchemy import create_engine, inspect, text
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnector:
    def __init__(self):
        db_url = os.getenv("DATABASE_URL")
        if db_url:
            self.engine = create_engine(db_url)
        else:
            self.engine = None

    def get_engine(self):
        return self.engine

    def execute(self, sql: str) -> tuple:
        if not self.engine:
            return [], []
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(sql))
                columns = list(result.keys())
                rows = [dict(zip(columns, row)) for row in result.fetchall()]
                return rows, columns
        except Exception as e:
            return [{"error": str(e)}], ["error"]

    def get_schema(self) -> list:
        if not self.engine:
            return []
        inspector = inspect(self.engine)
        tables = []
        for table_name in inspector.get_table_names():
            columns = []
            for col in inspector.get_columns(table_name):
                columns.append({
                    "name": col["name"],
                    "type": str(col["type"]),
                })
            tables.append({"table_name": table_name, "columns": columns})
        return tables
