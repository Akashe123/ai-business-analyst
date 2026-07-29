class DataAnalyzer:
    def summarize(self, rows: list, columns: list) -> dict:
        if not rows or not columns:
            return {"row_count": 0, "columns": [], "numeric_stats": {}, "top_values": {}}
        
        numeric_stats = {}
        top_values = {}
        
        for col in columns:
            numeric_col = []
            text_counts = {}
            
            for row in rows:
                val = row.get(col)
                if val is not None:
                    try:
                        numeric_col.append(float(val))
                    except (ValueError, TypeError):
                        text_counts[val] = text_counts.get(val, 0) + 1
            
            if numeric_col:
                numeric_stats[col] = {
                    "mean": round(sum(numeric_col) / len(numeric_col), 2),
                    "sum": round(sum(numeric_col), 2),
                    "min": min(numeric_col),
                    "max": max(numeric_col),
                    "count": len(numeric_col)
                }
            elif text_counts:
                sorted_vals = sorted(text_counts.items(), key=lambda x: -x[1])[:5]
                top_values[col] = dict(sorted_vals)
        
        return {
            "row_count": len(rows),
            "columns": columns,
            "numeric_stats": numeric_stats,
            "top_values": top_values
        }

    def recommend_chart(self, columns: list) -> str:
        if len(columns) < 2:
            return "table"
        return "bar"
