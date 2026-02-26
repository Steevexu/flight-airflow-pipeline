CREATE TABLE IF NOT EXISTS marts.daily_flight_metrics (
  day DATE PRIMARY KEY,
  orders INT,
  units INT,
  revenue NUMERIC(14,2)
);