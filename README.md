# ✈️ Flight Data Pipeline (Airflow + PostgreSQL + Docker)

## 📌 Overview
End-to-end batch data pipeline orchestrated with Airflow.

## 🏗 Architecture
- Docker Compose
- Airflow (LocalExecutor)
- PostgreSQL (staging + marts schema)
- Python ETL
- Data Quality checks

## 🚀 How to run
docker compose up -d

## 📊 DAG Flow
extract → validate → load → build mart

## 🧪 Data Quality
- null checks
- business rules validation
- positive quantities
- schema validation

## 🗄 Data Model
staging.flight_raw
marts.daily_flight_metrics