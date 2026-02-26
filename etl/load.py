import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

def get_conn():
    return psycopg2.connect(
        host=os.getenv("PG_HOST", "postgres"),
        port=int(os.getenv("PG_PORT", "5432")),
        dbname=os.getenv("PG_DB", "warehouse"),
        user=os.getenv("PG_USER", "airflow"),
        password=os.getenv("PG_PASSWORD", "airflow"),
    )

def load_sales_to_staging(df: pd.DataFrame) -> int:
    rows = df[["order_id","order_date","customer_id","product_id","quantity","unit_price","country"]].to_records(index=False)
    rows = [tuple(r) for r in rows]

    sql = """
      INSERT INTO staging.sales_raw(order_id, order_date, customer_id, product_id, quantity, unit_price, country)
      VALUES %s
    """
    with get_conn() as conn, conn.cursor() as cur:
        execute_values(cur, sql, rows, page_size=10_000)
        return len(rows)