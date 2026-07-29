from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS sales (
            id SERIAL PRIMARY KEY,
            region TEXT,
            product TEXT,
            sales_amount DECIMAL(10,2),
            quantity INT,
            sale_date DATE
        )
    """))
    conn.execute(text("""
        INSERT INTO sales (region, product, sales_amount, quantity, sale_date) VALUES
        ('North', 'Laptop', 15000.00, 10, '2024-01-15'),
        ('South', 'Laptop', 22000.00, 15, '2024-01-20'),
        ('East', 'Monitor', 8000.00, 20, '2024-02-01'),
        ('West', 'Monitor', 12000.00, 30, '2024-02-10'),
        ('North', 'Keyboard', 3000.00, 50, '2024-03-05'),
        ('South', 'Keyboard', 4500.00, 75, '2024-03-12'),
        ('East', 'Laptop', 18000.00, 12, '2024-03-20'),
        ('West', 'Laptop', 25000.00, 17, '2024-04-01'),
        ('North', 'Monitor', 6000.00, 15, '2024-04-10'),
        ('South', 'Monitor', 9000.00, 22, '2024-04-15')
    """))
    conn.commit()

print("✅ Sales table created with sample data!")
