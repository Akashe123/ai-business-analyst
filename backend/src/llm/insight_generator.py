import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

class InsightGenerator:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, question: str, data_summary: dict) -> str:
        prompt = f"""
You are a senior business analyst. Given a business question and data summary, 
provide clear, actionable insights.

Business Question: {question}

Data Summary:
- Row count: {data_summary.get('row_count', 0)}
- Columns: {', '.join(data_summary.get('columns', []))}
- Numeric stats: {data_summary.get('numeric_stats', {})}
- Top values: {data_summary.get('top_values', {})}

Provide exactly 3 insights:
1. Key finding
2. Trend or pattern
3. Actionable recommendation

Keep each to 1-2 sentences. Use numbers.
"""
        response = self.llm.invoke(prompt)
        return response.content
