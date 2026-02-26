import pandas as pd

def clean_flights(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["flight_date"] = pd.to_datetime(out["flight_date"]).dt.date
    out["departure_delay"] = out["departure_delay"].astype(int)
    out["arrival_delay"] = out["arrival_delay"].astype(int)
    out["distance_km"] = out["distance_km"].astype(int)
    out["origin"] = out["origin"].str.strip()
    out["destination"] = out["destination"].str.strip()
    return out