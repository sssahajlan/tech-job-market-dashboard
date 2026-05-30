import os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

PROCESSED_DATA_PATH = Path("data/processed")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")

connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
)

engine = create_engine(connection_url)

files_to_tables = {
    "jobs_dashboard.csv": "jobs_dashboard",
    "skills_dashboard.csv": "skills_dashboard",
    "skill_summary_dashboard.csv": "skill_summary_dashboard",
    "skills_by_role_dashboard.csv": "skills_by_role_dashboard",
    "role_summary_dashboard.csv": "role_summary_dashboard",
    "remote_summary_dashboard.csv": "remote_summary_dashboard",
    "salary_dashboard.csv": "salary_dashboard"
}

for file_name, table_name in files_to_tables.items():
    file_path = PROCESSED_DATA_PATH / file_name

    print(f"Loading {file_name} into table {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into {table_name}")

print("\nAll processed dashboard files loaded into PostgreSQL successfully!")