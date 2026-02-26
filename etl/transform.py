import pandas as pd

def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["order_date"] = pd.to_datetime(out["order_date"]).dt.date
    out["quantity"] = out["quantity"].astype(int)
    out["unit_price"] = out["unit_price"].astype(float)
    out["country"] = out["country"].astype(str).str.strip()
    return out