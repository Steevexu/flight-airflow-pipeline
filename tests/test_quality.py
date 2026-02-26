import pandas as pd
import pytest
import numpy as np

from etl.quality import validate_flights
from etl.transform import clean_flights

def test_validate_flights_ok():
    df = pd.DataFrame([
        {
            "flight_id": "F001",
            "flight_date": "2025-01-01",
            "origin": "CDG",
            "destination": "LHR",
            "airline": "AF",
            "departure_delay": 10,
            "arrival_delay": 5,
            "distance_km": 350,
        }
    ])
    df = clean_flights(df)
    validate_flights(df)  # doit passer sans exception

def test_validate_flights_missing_column_raises():
    df = pd.DataFrame([{"flight_id": "F001"}])
    with pytest.raises(ValueError):
        validate_flights(df)

def test_clean_flights_converts_types():
    df = pd.DataFrame([
        {
            "flight_id": "F001",
            "flight_date": "2025-01-01",
            "origin": " CDG ",
            "destination": "LHR ",
            "airline": "AF",
            "departure_delay": "10",
            "arrival_delay": "5",
            "distance_km": "350",
        }
    ])
    out = clean_flights(df)
    assert str(out.loc[0, "flight_date"]) == "2025-01-01"
    assert out.loc[0, "origin"] == "CDG"
    assert out.loc[0, "destination"] == "LHR"
    assert isinstance(out.loc[0, "departure_delay"], (int, np.integer))
    assert isinstance(out.loc[0, "distance_km"], (int, np.integer))