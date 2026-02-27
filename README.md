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
│   └── flight_etl.py                 # Airflow DAG (orchestration)
│
├── etl/
│   ├── __init__.py                   # Python package marker
│   ├── extract.py                    # CSV ingestion
│   ├── transform.py                  # Data cleaning & typing
│   ├── quality.py                    # Business validation rules
│   └── load.py                       # Load to PostgreSQL staging
│
├── dbt/
│   ├── flight_dbt/
│   │   ├── dbt_project.yml
│   │   ├── models/
│   │   │   ├── staging/
│   │   │   │   ├── stg_flights.sql
│   │   │   │   └── stg_flights.yml   # dbt schema tests
│   │   │   └── marts/
│   │   │       └── daily_flight_metrics.sql
│   │   ├── macros/                   # (optional / future use)
│   │   ├── target/                   # dbt build artifacts (gitignored)
│   │   └── dbt_packages/             # dbt dependencies (gitignored)
│   │
│   └── profiles/
│       └── profiles.yml              # Environment-based DB connection
│
├── sql/
│   └── 01_init.sql                   # Schema + staging table creation
│
├── data/
│   └── raw/
│       └── flights.csv               # Sample dataset
│
├── tests/
│   └── test_quality.py               # Unit tests (pytest)
│
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions CI pipeline
│
├── Dockerfile                        # Custom Airflow image (dbt included)
├── docker-compose.yml                # Local infrastructure setup
├── requirements-dev.txt              # Dev dependencies (pytest, ruff)
├── .gitignore
└── README.md
```

# 🚀 How to Run Locally

🏗 Start the Infrastructure

From the root of the project:
```bash
docker compose up --build
```

This will start:

- PostgreSQL
- Airflow Webserver
- Airflow Scheduler
  
🌐 Access Airflow UI
Open your browser:
```code
http://localhost:8080
```
Default credentials:
Username: airflow
Password: airflow

▶️ Run the Pipeline

1. Enable the DAG flight_etl
2. Click Trigger DAG
3. Monitor task execution

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
