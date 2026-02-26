# ✈️ Flight Data Pipeline

Airflow • PostgreSQL • dbt • Docker • GitHub Actions

---
![CI](https://github.com/Steevexu/Flight-Airflow-pipeline/actions/workflows/ci.yml/badge.svg)

# 📌 Overview

End-to-end batch data pipeline orchestrated with Apache Airflow, powered by PostgreSQL and transformed using dbt.

This project demonstrates a production-style Data Engineering architecture:

- Python ETL (validation + loading)

- Staging / Marts modeling

- dbt transformations & tests

- Containerized infrastructure

- CI with GitHub Actions
  
---

# 🏗 Architecture

```code
CSV → Python Validation → Postgres (staging) → dbt (staging models)
      → dbt (marts) → Data Quality Tests
```
## Stack

- 🐳 Docker & Docker Compose
- 🛠 Apache Airflow (LocalExecutor)
- 🗄 PostgreSQL 16
- 🔄 dbt (postgres adapter)
- 🧪 dbt tests
- 🧹 Ruff (lint)
- ⚙ GitHub Actions CI

# 📂 Project Structure

```code
Flight-Airflow-pipeline/
│
├── dags/
│   └── flight_etl.py
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── quality.py
│   └── load.py
│
├── dbt/
│   ├── flight_dbt/
│   │   ├── dbt_project.yml
│   │   └── models/
│   │       ├── staging/
│   │       │   └── stg_flights.sql
│   │       └── marts/
│   │           └── daily_flight_metrics.sql
│   └── profiles/
│       └── profiles.yml
│
├── sql/
│   └── 01_init.sql
│
├── data/raw/
│   └── flights.csv
│
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/ci.yml
```

# 🚀 How to Run Locally

```bash
docker compose up -d
```
1️⃣ Start infrastructure

Airflow UI:
👉 http://localhost:8080
Login: admin / admin

2️⃣ Trigger DAG

Enable and trigger:
```code
flight_etl
```

Pipeline flow:
```code
extract_transform_validate
    ↓
load_staging
    ↓
dbt_run
    ↓
dbt_test
```

# 🗄 Data Model

## 🔹 Staging Layer
```text
staging.flight_raw
```

Raw ingested flight records.

## 🔹 dbt Staging Model
```text
staging.stg_flights
```

Cleaned view over raw data.

## 🔹 Mart Layer

```text
marts.daily_flight_metrics
```


Aggregated KPIs:

- total flights
- average departure delay
- average arrival delay
- total distance

# 🧪 Data Quality
## Python Validation

- Required columns
- Null checks
- Schema validation

## dbt Tests

- not_null
- (extensible to unique / relationships)

# ⚙ Continuous Integration

GitHub Actions automatically:

- Lints Python code
- Initializes PostgreSQL schema
- Runs pytest
- Executes dbt debug
- Runs dbt run
- Executes dbt test

Every push to main triggers the CI pipeline.

# 💡 Why This Project?

This project showcases:

- ✔Orchestration with Airflow
- ✔ SQL modeling best practices (staging → marts)
- ✔ dbt transformations and testing
- ✔ Containerized data infrastructure
- ✔ CI automation
- ✔ Production-oriented architecture

It reflects real-world Data Engineering workflows.

# 📈 Next Improvements

- Add dbt snapshots (SCD Type 2)
- Add dashboard layer (Metabase)
- Add data observability metrics
- Add incremental models

# 👤 Author

Steeve Xu
Data Engineer
Toulouse, France
