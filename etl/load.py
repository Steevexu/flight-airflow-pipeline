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


def _to_python_records(df):
    """Convert pandas/numpy scalars to Python native types for psycopg2."""
    import numpy as np
    import pandas as pd

    df = df.copy()

    # Replace NaN/NaT with None (psycopg2-friendly)
    df = df.where(pd.notnull(df), None)

    def conv(x):
        if isinstance(x, np.integer):
            return int(x)
        if isinstance(x, np.floating):
            return float(x)
        if isinstance(x, np.bool_):
            return bool(x)
        # pandas Timestamp -> python datetime
        if hasattr(x, "to_pydatetime"):
            return x.to_pydatetime()
        return x

    return [tuple(conv(v) for v in row) for row in df.itertuples(index=False, name=None)]


def load_flights_to_staging(df):
    # Keep the column order aligned with the INSERT statement
    cols = [
        "flight_id",
        "flight_date",
        "origin",
        "destination",
        "airline",
        "departure_delay",
        "arrival_delay",
        "distance_km",
    ]
    rows = _to_python_records(df[cols])

    sql = """
      INSERT INTO staging.flight_raw
      (flight_id, flight_date, origin, destination, airline,
       departure_delay, arrival_delay, distance_km)
      VALUES %s
    """

    with get_conn() as conn, conn.cursor() as cur:
        execute_values(cur, sql, rows)
        return len(rows)