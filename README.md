<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Next.js-14-black?style=for-the-badge&logo=next.js" alt="Next.js">
  <img src="https://img.shields.io/badge/FastAPI-0.115-teal?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-Neon-4169E1?style=for-the-badge&logo=postgresql" alt="Neon">
  <img src="https://img.shields.io/badge/Groq-AI-F97316?style=for-the-badge&logo=groq" alt="Groq">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT">
  
  <br><br>
  
  <h1>💼 AI Business Analyst Assistant</h1>
  <p><strong>Upload your data. Ask questions in plain English. Get instant insights.</strong></p>
  
  <p>
    An intelligent assistant that understands natural language business questions, generates SQL queries, 
    analyzes data, and produces beautiful visualizations — powered by AI.
  </p>
  
  <br>
  
  <table>
    <tr>
      <td><img src="docs/screenshots/dashboard.png" alt="Dashboard" width="400"></td>
      <td><img src="docs/screenshots/chart.png" alt="Charts" width="400"></td>
    </tr>
    <tr>
      <td align="center"><em>📊 Main Dashboard</em></td>
      <td align="center"><em>📈 Interactive Visualizations</em></td>
    </tr>
  </table>
</div>

<br>

<p align="center">
  <a href="#features">✨ Features</a> •
  <a href="#tech-stack">🛠️ Tech Stack</a> •
  <a href="#architecture">🏗️ Architecture</a> •
  <a href="#getting-started">🚀 Getting Started</a> •
  <a href="#api-reference">📡 API</a> •
  <a href="#screenshots">📸 Screenshots</a> •
  <a href="#documentation">📄 Docs</a>
</p>

---

## ✨ Features

<div align="center">
  <table>
    <tr>
      <td align="center" width="200">
        <h3>🗣️</h3>
        <b>Natural Language</b>
        <p>Ask questions in plain English</p>
      </td>
      <td align="center" width="200">
        <h3>🧠</h3>
        <b>AI-Powered SQL</b>
        <p>Auto-generates accurate queries</p>
      </td>
      <td align="center" width="200">
        <h3>📊</h3>
        <b>Charts</b>
        <p>Bar, line & pie visualizations</p>
      </td>
    </tr>
    <tr>
      <td align="center" width="200">
        <h3>📁</h3>
        <b>File Upload</b>
        <p>CSV & Excel supported</p>
      </td>
      <td align="center" width="200">
        <h3>💡</h3>
        <b>Smart Insights</b>
        <p>AI-generated recommendations</p>
      </td>
      <td align="center" width="200">
        <h3>🌙</h3>
        <b>Dark UI</b>
        <p>Modern glass-morphism design</p>
      </td>
    </tr>
  </table>
</div>

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Next.js 14 + React 18 | UI framework & rendering |
| **Charts** | Recharts | Interactive data visualization |
| **Backend** | FastAPI (Python) | REST API server |
| **AI/LLM** | Groq (LLaMA 3.3-70B) | Natural language → SQL |
| **Orchestration** | LangChain | LLM prompt management |
| **Database** | Neon (PostgreSQL) | Serverless data storage |
| **ORM** | SQLAlchemy | Database connectivity |
| **Hosting** | Vercel | CI/CD & deployment |

---

## 🏗️ Architecture

┌──────────────────────────────────────────────────────┐ │ User Browser │ │ http://localhost:3000 │ └───────────────────────┬──────────────────────────────┘ │ HTTP Requests ▼ ┌──────────────────────────────────────────────────────┐ │ Next.js Frontend (Vercel) │ │ ┌─────────┐ ┌──────────┐ ┌────────────────────┐ │ │ │ Upload │ │ Query │ │ Charts & Tables │ │ │ │ CSV │ │ Input │ │ Visualization │ │ │ └────┬─────┘ └────┬─────┘ └────────────────────┘ │ └───────┼──────────────┼───────────────────────────────┘ │ │ ▼ ▼ ┌──────────────────────────────────────────────────────┐ │ FastAPI Backend (Vercel) │ │ ┌──────────┐ ┌──────────┐ ┌────────────────┐ │ │ │ /upload │ │ /ask │ │ /schema │ │ │ │ File→DB │ │ NLP→SQL │ │ Table Info │ │ │ └────┬─────┘ └────┬─────┘ └────────────────┘ │ │ │ │ │ │ ▼ ▼ │ │ ┌───────────────────────────────────────────┐ │ │ │ LangChain + Groq AI │ │ │ │ Natural Language → SQL Query Generator │ │ │ │ Data Analysis → Business Insights │ │ │ └───────────────────────────────────────────┘ │ └──────────────────────┬───────────────────────────────┘ │ ▼ ┌──────────────────────────────────────────────────────┐ │ Neon Serverless PostgreSQL │ │ Cloud Database │ └──────────────────────────────────────────────────────┘



### Data Flow

1. **User Input** → Upload CSV/Excel or type a question
2. **AI Processing** → Groq LLaMA 3.3-70B understands the question
3. **SQL Generation** → LangChain generates PostgreSQL query from schema
4. **Query Execution** → SQLAlchemy runs query on Neon DB
5. **Analysis** → Computes statistics & patterns
6. **Insights** → AI generates business recommendations
7. **Visualization** → Recharts renders interactive charts
8. **Display** → Results shown in dark-theme UI

---

## 🚀 Getting Started

### Prerequisites

| Requirement | Version | Get It |
|------------|---------|--------|
| Python | 3.11+ | [python.org](https://python.org) |
| Node.js | 18+ | [nodejs.org](https://nodejs.org) |
| Groq API Key | Free | [console.groq.com/keys](https://console.groq.com/keys) |
| Neon Database | Free Tier | [console.neon.tech](https://console.neon.tech) |

### 1. Clone & Install

```bash
git clone https://github.com/Akashe123/ai-business-analyst.git
cd ai-business-analyst

# Backend
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install
2. Configure Environment
Create backend/.env:


GROQ_API_KEY=gsk_your_groq_api_key_here
DATABASE_URL=postgresql://user:pass@ep-xxx.aws.neon.tech/neondb?sslmode=require
3. Run the App
Terminal 1 — Backend:


cd backend
venv\Scripts\activate
uvicorn main:app --reload --port 8000
Terminal 2 — Frontend:


cd frontend
npm run dev
4. Open in Browser
👉 http://localhost:3000

📡 API Reference
Method	Endpoint	Description
POST	/api/ask	Ask a business question
POST	/api/upload	Upload CSV/Excel file
GET	/api/tables	List all database tables
GET	/api/schema	Get database schema
GET	/api/health	Health check
Example: POST /api/ask
Request:


{
  "question": "Show me total sales by region"
}
Response:


{
  "sql": "SELECT region, SUM(sales_amount) AS total_sales FROM sales GROUP BY region ORDER BY total_sales DESC",
  "data": [
    {"region": "West", "total_sales": "74000.00"},
    {"region": "South", "total_sales": "71000.00"},
    {"region": "East", "total_sales": "52000.00"},
    {"region": "North", "total_sales": "48000.00"}
  ],
  "columns": ["region", "total_sales"],
  "insights": "1. Key finding: Total sales across all regions is $245,000...\n2. Trend: West leads with 30% of total sales...\n3. Recommendation: Focus marketing on North region...",
  "chart_recommendation": "bar"
}
📸 Screenshots
<div align="center"> <table> <tr> <td><img src="docs/screenshots/dashboard.png" alt="Dashboard" width="350"></td> <td><img src="docs/screenshots/upload.png" alt="Upload" width="350"></td> </tr> <tr> <td align="center"><em>🏠 Main Dashboard</em></td> <td align="center"><em>📁 Upload CSV/Excel</em></td> </tr> <tr> <td><img src="docs/screenshots/query.png" alt="Query" width="350"></td> <td><img src="docs/screenshots/chart.png" alt="Chart" width="350"></td> </tr> <tr> <td align="center"><em>🗣️ Ask Questions</em></td> <td align="center"><em>📊 Interactive Charts</em></td> </tr> <tr> <td colspan="2"><img src="docs/screenshots/insights.png" alt="Insights" width="700"></td> </tr> <tr> <td colspan="2" align="center"><em>💡 AI-Generated Insights</em></td> </tr> </table> </div>
🧪 Sample Queries
"Show me total sales by region"
"What's the profit by product category?"
"Which product has the highest quantity sold?"
"Show me monthly sales trend"
"Compare sales across regions for each product"
"What are the top 5 best-selling products?"
"Show me total revenue by month"
"Which region has the highest profit margin?"
🗺️ Project Structure

ai-business-analyst/
├── backend/                          # Python FastAPI backend
│   ├── src/
│   │   ├── llm/
│   │   │   ├── sql_generator.py      # NLP → SQL conversion
│   │   │   └── insight_generator.py  # Business insights
│   │   ├── database/
│   │   │   └── connector.py          # DB connection
│   │   └── analysis/
│   │       └── analyzer.py           # Data analysis
│   ├── main.py                       # FastAPI server
│   ├── seed_data.py                  # Sample data seeder
│   └── requirements.txt
├── frontend/                         # Next.js frontend
│   ├── pages/
│   │   └── index.tsx                 # Main UI
│   ├── styles/
│   │   └── globals.css               # Global styles
│   ├── package.json
│   └── next.config.js
├── docs/                             # Documentation
│   ├── screenshots/                  # Website screenshots
│   ├── documentation.tex             # LaTeX source
│   └── documentation.pdf             # Compiled PDF report
├── sample_sales.csv                  # Sample data
├── README.md                         # You are here
└── .gitignore
🌐 Deployment
Backend:


cd backend
npm i -g vercel
vercel --prod
Set env vars: GROQ_API_KEY, DATABASE_URL

Frontend:


cd frontend
vercel --prod
Set env var: NEXT_PUBLIC_API_URL = your backend URL

📄 Documentation
<p align="center"> <a href="docs/documentation.pdf"> <img src="https://img.shields.io/badge/📄_Download_PDF_Report-blue?style=for-the-badge&logo=adobe" alt="PDF"> </a> </p>
The documentation includes:

📐 System architecture & data flow diagrams
🛠️ Complete technology stack details
📡 Full API reference with examples
📸 All screenshots in high resolution
🚀 Deployment guide for Vercel
🧠 How It Works

User: "Show me total sales by region"
           │
           ▼
    ┌──────────────┐
    │  Groq AI     │  ← Understands intent
    │  (LLaMA 3.3) │
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │  Generate    │  ← Creates SQL from schema
    │  SQL Query   │
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │  Execute on  │  ← Queries Neon PostgreSQL
    │  Database    │
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │  Analyze     │  ← Computes stats & trends
    │  Results     │
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │  Generate    │  ← AI writes insights
    │  Insights    │
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │  Render      │  ← Charts + table + insights
    │  UI          │
    └──────────────┘
📋 License
This project is licensed under the MIT License.

🙏 Acknowledgments
Groq — Fast LLM inference
Neon — Serverless PostgreSQL
LangChain — AI orchestration framework
Vercel — Hosting & deployment
Recharts — Charting library
<div align="center"> <p>Built with ❤️ by <a href="https://github.com/Akashe123">Akashe123</a></p> <p> <a href="https://github.com/Akashe123/ai-business-analyst/issues">🐛 Report Bug</a> • <a href="https://github.com/Akashe123/ai-business-analyst/issues">✨ Request Feature</a> • <a href="docs/documentation.pdf">📄 Documentation</a> </p> <p> <img src="https://img.shields.io/github/stars/Akashe123/ai-business-analyst?style=social" alt="Stars"> <img src="https://img.shields.io/github/forks/Akashe123/ai-business-analyst?style=social" alt="Forks"> </p> </div> ```