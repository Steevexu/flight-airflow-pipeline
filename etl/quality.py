import pandas as pd

REQUIRED_COLS = ["order_id", "order_date", "customer_id", "product_id", "quantity", "unit_price", "country"]

def validate_sales(df: pd.DataFrame) -> None:
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    if df[["order_id", "order_date", "customer_id", "product_id"]].isna().any().any():
        raise ValueError("Nulls found in required id/date columns")

    if (df["quantity"] <= 0).any():
        raise ValueError("quantity must be > 0")

    if (df["unit_price"] <= 0).any():
        raise ValueError("unit_price must be > 0")