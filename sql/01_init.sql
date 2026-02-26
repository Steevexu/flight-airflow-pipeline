CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS marts;

CREATE TABLE IF NOT EXISTS staging.flight_raw (
  flight_id        TEXT,
  flight_date      DATE,
  origin           TEXT,
  destination      TEXT,
  airline          TEXT,
  departure_delay  INT,
  arrival_delay    INT,
  distance_km      INT,
  ingested_at      TIMESTAMP DEFAULT NOW()
);