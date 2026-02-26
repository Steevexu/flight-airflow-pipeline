from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from etl.extract import read_csv
from etl.transform import clean_sales
from etl.quality import validate_sales
from etl.load import load_sales_to_staging, get_conn

CSV_PATH = "/opt/airflow/data/raw/sales.csv"

def task_extract_transform_validate(**_):
    df = read_csv(CSV_PATH)
    df = clean_sales(df)
    validate_sales(df)
    # stocker temporairement en parquet dans le volume partagé
    df.to_parquet("/opt/airflow/data/raw/_clean_sales.parquet", index=False)

def task_load(**_):
    import pandas as pd
    df = pd.read_parquet("/opt/airflow/data/raw/_clean_sales.parquet")
    n = load_sales_to_staging(df)
    print(f"Loaded {n} rows into staging.sales_raw")

def task_build_mart(**_):
    sql = """
    INSERT INTO marts.daily_revenue(day, orders, units, revenue)
    SELECT
      order_date AS day,
      COUNT(DISTINCT order_id) AS orders,
      SUM(quantity) AS units,
      SUM(quantity * unit_price)::numeric(14,2) AS revenue
    FROM staging.sales_raw
    GROUP BY order_date
    ON CONFLICT (day) DO UPDATE
      SET orders = EXCLUDED.orders,
          units = EXCLUDED.units,
          revenue = EXCLUDED.revenue;
    """
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(sql)

with DAG(
    dag_id="retail_etl",
    start_date=datetime(2025, 1, 1),
    schedule=None,   # manuel (tu pourras mettre @daily ensuite)
    catchup=False,
    tags=["portfolio", "data-engineering"],
) as dag:
    extract_transform_validate = PythonOperator(
        task_id="extract_transform_validate",
        python_callable=task_extract_transform_validate,
    )

    load_staging = PythonOperator(
        task_id="load_staging",
        python_callable=task_load,
    )

    build_mart = PythonOperator(
        task_id="build_mart",
        python_callable=task_build_mart,
    )

    extract_transform_validate >> load_staging >> build_mart