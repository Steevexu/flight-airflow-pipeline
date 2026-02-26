from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from etl.extract import read_csv
from etl.transform import clean_flights
from etl.quality import validate_flights
from etl.load import load_flights_to_staging

CSV_PATH = "/opt/airflow/data/raw/flights.csv"
DBT_DIR = "/opt/airflow/dbt/flight_dbt"
PROFILES_DIR = "/opt/airflow/dbt/profiles"

def task_extract_transform_validate(**_):
    df = read_csv(CSV_PATH)
    df = clean_flights(df)
    validate_flights(df)
    df.to_parquet("/opt/airflow/data/raw/_clean_flights.parquet", index=False)

def task_load(**_):
    import pandas as pd
    df = pd.read_parquet("/opt/airflow/data/raw/_clean_flights.parquet")
    n = load_flights_to_staging(df)
    print(f"Loaded {n} rows into staging.flight_raw")

with DAG(
    dag_id="flight_etl",
    start_date=datetime(2025, 1, 1),
    schedule=None,
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

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"dbt run --project-dir {DBT_DIR} --profiles-dir {PROFILES_DIR}",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"dbt test --project-dir {DBT_DIR} --profiles-dir {PROFILES_DIR}",
    )

    extract_transform_validate >> load_staging >> dbt_run >> dbt_test