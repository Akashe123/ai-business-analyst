import { useState, useRef, useEffect } from "react";
import {
  BarChart, Bar, LineChart, Line,
  XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, PieChart, Pie, Cell, Legend
} from "recharts";

const COLORS = ["#60a5fa", "#34d399", "#fbbf24", "#f472b6", "#a78bfa", "#fb923c"];

export default function Home() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [uploading, setUploading] = useState(false);
  const [uploadMsg, setUploadMsg] = useState("");
  const [tables, setTables] = useState<string[]>([]);
  const fileRef = useRef<HTMLInputElement>(null);
  const resultsRef = useRef<HTMLDivElement>(null);

  useEffect(() => { loadTables(); }, []);

  const ask = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setError("");
    try {
      const res = await fetch("/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      if (!res.ok) throw new Error(`Error: ${res.status}`);
      const data = await res.json();
      setResult(data);
      setTimeout(() => resultsRef.current?.scrollIntoView({ behavior: "smooth", block: "start" }), 100);
    } catch (err: any) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  const uploadFile = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setUploading(true);
    setUploadMsg("");
    setError("");
    try {
      const formData = new FormData();
      formData.append("file", file);
      const res = await fetch("/api/upload", { method: "POST", body: formData });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Upload failed");
      setUploadMsg(data.message);
      loadTables();
    } catch (err: any) {
      setError(err.message);
    } finally {
      setUploading(false);
      if (fileRef.current) fileRef.current.value = "";
    }
  };

  const loadTables = async () => {
    try {
      const res = await fetch("/api/tables");
      const data = await res.json();
      setTables((data.tables || []).map((t: any) => t.table_name));
    } catch {}
  };

  const renderChart = () => {
    if (!result?.data?.length || result.columns.length < 2) return null;
    const data = result.data.slice(0, 50);
    const xKey = result.columns[0];
    const yKey = result.columns[1];
    const chartType = result.chart_recommendation;

    return (
      <ResponsiveContainer width="100%" height={360}>
        {chartType === "line" ? (
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="rgba(148,163,184,0.1)" />
            <XAxis dataKey={xKey} stroke="#64748b" tick={{ fill: "#94a3b8" }} />
            <YAxis stroke="#64748b" tick={{ fill: "#94a3b8" }} />
            <Tooltip
              contentStyle={{
                background: "#1e293b",
                border: "1px solid rgba(148,163,184,0.15)",
                borderRadius: 8,
                color: "#e2e8f0",
              }}
            />
            <Line type="monotone" dataKey={yKey} stroke="#60a5fa" strokeWidth={3} dot={{ fill: "#60a5fa", r: 4 }} />
          </LineChart>
        ) : chartType === "pie" ? (
          <PieChart>
            <Pie data={data} dataKey={yKey} nameKey={xKey} cx="50%" cy="50%" outerRadius={130} label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}>
              {data.map((_, i) => <Cell key={i} fill={COLORS[i % COLORS.length]} />)}
            </Pie>
            <Tooltip contentStyle={{ background: "#1e293b", border: "1px solid rgba(148,163,184,0.15)", borderRadius: 8, color: "#e2e8f0" }} />
            <Legend />
          </PieChart>
        ) : (
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="rgba(148,163,184,0.1)" />
            <XAxis dataKey={xKey} stroke="#64748b" tick={{ fill: "#94a3b8" }} />
            <YAxis stroke="#64748b" tick={{ fill: "#94a3b8" }} />
            <Tooltip contentStyle={{ background: "#1e293b", border: "1px solid rgba(148,163,184,0.15)", borderRadius: 8, color: "#e2e8f0" }} />
            <Bar dataKey={yKey} radius={[6, 6, 0, 0]}>
              {data.map((_, i) => <Cell key={i} fill={COLORS[i % COLORS.length]} />)}
            </Bar>
          </BarChart>
        )}
      </ResponsiveContainer>
    );
  };

  return (
    <div className="container">
      <header className="header">
        <h1>💼 AI Business Analyst</h1>
        <p>Upload your data, ask questions — get instant insights</p>
      </header>

      {/* Upload */}
      <div className="card upload-card">
        <h3>📁 Upload Your Data</h3>
        <div className="upload-area">
          <input type="file" ref={fileRef} onChange={uploadFile} accept=".csv,.xls,.xlsx" />
          <button onClick={() => fileRef.current?.click()} disabled={uploading} className="upload-btn">
            {uploading ? "⏳ Uploading..." : "📤 Choose CSV or Excel File"}
          </button>
          {uploadMsg && <p className="success">{uploadMsg}</p>}
        </div>
        {tables.length > 0 && (
          <p className="tables-note">📊 Tables: {tables.join(" · ")}</p>
        )}
      </div>

      {/* Ask */}
      <div className="input-area">
        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); ask(); } }}
          placeholder='Ask a business question… e.g. "Show me total sales by region"'
          rows={2}
        />
        <button onClick={ask} disabled={loading || !question.trim()} className={loading ? "loading-btn" : ""}>
          {loading ? "🤔 Analyzing..." : "🔍 Ask"}
        </button>
      </div>

      {error && <div className="error">❌ {error}</div>}

      {/* Results */}
      {result && (
        <div ref={resultsRef}>
          {result.data?.length > 0 && (
            <div className="card chart-card">
              <h3>📊 Visualization</h3>
              {renderChart()}
            </div>
          )}
          <div className="card">
            <h3>📝 Generated SQL</h3>
            <pre>{result.sql}</pre>
          </div>
          <div className="card">
            <h3>📋 Data ({result.data.length} rows)</h3>
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>{result.columns.map((c: string) => <th key={c}>{c}</th>)}</tr>
                </thead>
                <tbody>
                  {result.data.slice(0, 20).map((row: any, i: number) => (
                    <tr key={i}>
                      {result.columns.map((c: string) => <td key={c}>{row[c]?.toString() ?? ""}</td>)}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
          <div className="card insights">
            <h3>💡 Key Insights</h3>
            {result.insights.split("\n").filter((l: string) => l.trim()).map((line: string, i: number) => (
              <p key={i}>{line}</p>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
