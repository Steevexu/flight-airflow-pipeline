def validate_flights(df):
    required = [
        "flight_id",
        "flight_date",
        "origin",
        "destination",
        "airline",
        "departure_delay",
        "arrival_delay",
        "distance_km",
    ]

    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    if df["flight_id"].isna().any():
        raise ValueError("Null flight_id detected")