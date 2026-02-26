import os
import psycopg2
from psycopg2.extras import execute_values

def get_conn():
    return psycopg2.connect(
        host="postgres",
        port=5432,
        dbname="warehouse",
        user="airflow",
        password="airflow",
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