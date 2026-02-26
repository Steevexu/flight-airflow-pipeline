import os
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

def load_flights_to_staging(df):
    rows = df.to_records(index=False)
    rows = [tuple(r) for r in rows]

    sql = """
      INSERT INTO staging.flight_raw
      (flight_id, flight_date, origin, destination, airline,
       departure_delay, arrival_delay, distance_km)
      VALUES %s
    """

    with get_conn() as conn, conn.cursor() as cur:
        execute_values(cur, sql, rows)
        return len(rows)