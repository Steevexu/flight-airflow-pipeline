CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS marts;

CREATE TABLE IF NOT EXISTS staging.flight_raw (
  order_id        TEXT,
  order_date      DATE,
  customer_id     TEXT,
  product_id      TEXT,
  quantity        INT,
  unit_price      NUMERIC(10,2),
  country         TEXT,
  ingested_at     TIMESTAMP DEFAULT NOW()
);