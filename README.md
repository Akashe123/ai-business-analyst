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

## 🏗️ System Architecture


                     ┌─────────────────────┐
                     │     🌐 USER         │
                     │   localhost:3000     │
                     └──────────┬──────────┘
                                │
                      ┌─────────┴─────────┐
                      │   Ask Question     │
                      │   Upload File      │
                      └─────────┬─────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────┐ │ ⚛️ FRONTEND (Next.js) │ │ │ │ ┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐ │ │ │ 📁 Upload │ │ 💬 Query │ │ 📊 Charts │ │ │ │ CSV/Excel │ │ Input Box │ │ Bar • Line • Pie │ │ │ └──────┬───────┘ └──────┬───────┘ └──────────────────────┘ │ │ │ │ │ └─────────┼──────────────────┼───────────────────────────────────────┘ │ │ │ HTTP POST │ ▼ ▼ ┌───────────────────────────────────────────────────────────────────┐ │ 🐍 BACKEND (FastAPI) │ │ │ │ ┌───────────────────────────────────────────────────────────┐ │ │ │ 🧠 AI ENGINE │ │ │ │ │ │ │ │ ┌──────────────┐ ┌─────────────────────────┐ │ │ │ │ │ Groq AI │───────▶│ LangChain Pipeline │ │ │ │ │ │ LLaMA 3.3 │ │ Question → SQL → │ │ │ │ │ └──────────────┘ │ Execute → Analyze → │ │ │ │ │ │ Insights → Chart │ │ │ │ │ └─────────────────────────┘ │ │ │ └───────────────────────────────────────────────────────────┘ │ │ │ │ └──────────────────────────────┼────────────────────────────────────┘ │ │ SQL Query ▼ ┌───────────────────────────────────────────────────────────────────┐ │ 🗄️ DATABASE (Neon PostgreSQL) │ │ │ │ ┌───────────────────────────────────────────────────────────┐ │ │ │ │ │ │ │ Tables: sales │ customers │ products │ ... │ │ │ │ │ │ │ │ Connection: SQLAlchemy + psycopg2 │ │ │ │ │ │ │ └──────────────────────────────────────────────────────────┘ │ └───────────────────────────────────────────────────────────────────┘



---

### 🔄 Data Flow

USER AI DATABASE RESULT ──── ── ──────── ──────

┌─────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐ │"Show me │ │ Groq │ │ Neon │ │ Chart │ │ sales by│─────────▶│ AI │─────────▶│ PostgreSQL│──────▶│ + │ │ region" │ │ Generate │ │ Execute │ │ Insights│ └─────────┘ │ SQL │ │ Query │ └─────────┘ └──────────┘ └──────────┘ │ │ ▼ ▼ ┌──────────┐ ┌──────────┐ │ SELECT │ │ West: │ │ region, │ │ $74,000 │ │ SUM(...) │ │ South: │ │ FROM │ │ $71,000 │ │ sales... │ │ East: │ └──────────┘ │ $52,000 │ └──────────┘



---

### 📡 API Request-Response

POST /api/ask ═══════════════════════════════════════════════════════════

REQUEST RESPONSE ─────── ────────

┌──────────────────┐ ┌──────────────────────────────────┐ │ { │ │ { │ │ "question": │ │ "sql": "SELECT region, │ │ "Show me total │ ▶ │ SUM(sales_amount)...", │ │ sales by │ │ "data": [ │ │ region" │ │ {"region": "West", │ │ } │ │ "total_sales": 74000}, │ └──────────────────┘ │ {"region": "South", │ │ "total_sales": 71000}, │ │ ... │ │ ], │ │ "columns": ["region", │ │ "total_sales"], │ │ "insights": "1. Key finding: │ │ West leads with $74,000...", │ │ "chart_recommendation": "bar" │ │ } │ └──────────────────────────────────┘



---

### 🧠 AI Processing Pipeline


                ┌─────────────────────────────────────┐
                │      INPUT PROCESSING               │
                │                                     │
                │  "Show me total sales by region"    │
                │         │                           │
                │         ▼                           │
                │  ┌─────────────┐                    │
                │  │ Tokenize    │                    │
                │  │ & Parse     │                    │
                │  └──────┬──────┘                    │
                │         ▼                           │
                │  ┌─────────────┐                    │
                │  │ Identify    │  "total sales"     │
                │  │ Intent      │  → SUM()          │
                │  └──────┬──────┘  "by region"       │
                │         │         → GROUP BY        │
                │         ▼                           │
                │  ┌─────────────┐                    │
                │  │ Map to      │  sales.region      │
                │  │ Schema      │  sales.sales_amount│
                │  └──────┬──────┘                    │
                │         ▼                           │
                │  ┌─────────────┐                    │
                │  │ Generate    │  SELECT region,    │
                │  │ SQL Query   │  SUM(sales_amount) │
                │  │             │  FROM sales        │
                │  │             │  GROUP BY region   │
                │  └─────────────┘                    │
                └─────────────────────────────────────┘


---

### 🗺️ Deployment Architecture

┌──────────────────────────────────────────────────────────────┐ │ GITHUB REPOSITORY │ │ │ │ ┌──────────────────────────────────────────────────────┐ │ │ │ Akashe123/ai-business-analyst │ │ │ │ │ │ │ │ 📁 backend/ → FastAPI Python code │ │ │ │ 📁 frontend/ → Next.js React code │ │ │ │ 📁 docs/ → Documentation & screenshots │ │ │ │ 📄 README.md → Project overview │ │ │ └──────────────────────────────────────────────────────┘ │ └──────────────────────────┬───────────────────────────────────┘ │ git push ▼ ┌──────────────────────────────────────────────────────────────┐ │ VERCEL CLOUD │ │ │ │ ┌──────────────────────┐ ┌──────────────────────────┐ │ │ │ 🔵 FRONTEND │ │ 🟢 BACKEND │ │ │ │ │ │ │ │ │ │ ai-business-analyst│ │ fastapi-api.vercel.app │ │ │ │ .vercel.app │ │ │ │ │ │ │ │ Environment: │ │ │ │ Framework: Next.js │ │ • GROQ_API_KEY │ │ │ │ Build: npm run │◄──▶│ • DATABASE_URL │ │ │ │ build │ │ │ │ │ └──────────────────────┘ └───────────┬──────────────┘ │ └───────────────────────────────────────────┼──────────────────┘ │ ▼ ┌──────────────────────────────┐ │ 🗄️ NEON DATABASE │ │ │ │ ep-xxx.aws.neon.tech │ │ │ │ Serverless PostgreSQL │ │ Auto-scale • Branching │ └──────────────────────────────┘



---

### 🏛️ Technology Stack

┌──────────────────────────────────────────────────────────────┐ │ TECHNOLOGY STACK │ ├────────────┬──────────────────────┬─────────────────────────┤ │ LAYER │ TECHNOLOGY │ PURPOSE │ ├────────────┼──────────────────────┼─────────────────────────┤ │ 🎨 UI │ Next.js 14 + React │ User Interface │ │ 📊 Charts │ Recharts + D3.js │ Data Visualization │ │ 🌐 API │ FastAPI (Python) │ REST API Server │ │ 🧠 AI │ Groq (LLaMA 3.3) │ NLP → SQL Generation │ │ 🔗 Chain │ LangChain │ LLM Orchestration │ │ 💾 DB │ Neon PostgreSQL │ Data Storage │ │ 🔌 ORM │ SQLAlchemy │ Database Connection │ │ ☁️ Host │ Vercel │ Deployment & CDN │ └────────────┴──────────────────────┴─────────────────────────┘

📋 License
This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

<div align="center">

┌─────────────────────────────────────────────────────────────────┐ │ ACKNOWLEDGMENTS │ ├──────────────┬──────────────────────────────────────────────────┤ │ 🏆 │ Groq — Fast LLM inference │ │ 🏆 │ Neon — Serverless PostgreSQL │ │ 🏆 │ LangChain — AI orchestration framework │ │ 🏆 │ Vercel — Hosting & deployment │ │ 🏆 │ Recharts — Charting library │ └──────────────┴──────────────────────────────────────────────────┘


</div>

---

<div align="center">

┌──────────────────────────────────────────────────────────────┐ │ │ │ 💼 AI Business Analyst Assistant │ │ │ │ Built with ❤️ by Akashe123 │ │ │ │ ┌─────────────────────────────────────────────┐ │ │ │ 🐛 Report Bug • ✨ Request Feature │ │ │ │ 📄 Documentation │ │ │ └─────────────────────────────────────────────┘ │ │ │ │ ⭐ Stars │ 🍴 Forks │ │ │ └──────────────────────────────────────────────────────────────┘


</div>

<p align="center">
  <a href="https://github.com/Akashe123/ai-business-analyst/issues">🐛 Report Bug</a>
  •
  <a href="https://github.com/Akashe123/ai-business-analyst/issues">✨ Request Feature</a>
  •
  <a href="docs/documentation.pdf">📄 Documentation</a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Akashe123/ai-business-analyst?style=social" alt="Stars">
  <img src="https://img.shields.io/github/forks/Akashe123/ai-business-analyst?style=social" alt="Forks">
</p>
