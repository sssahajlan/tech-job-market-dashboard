import pandas as pd
from pathlib import Path

CLEANED_DATA_PATH = Path("data/cleaned")
PROCESSED_DATA_PATH = Path("data/processed")
PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

# Load cleaned files
jobs = pd.read_csv(CLEANED_DATA_PATH / "filtered_tech_jobs_with_skills.csv")
skills_long = pd.read_csv(CLEANED_DATA_PATH / "technical_skills_long.csv")

print("Files loaded successfully!")
print("Jobs shape:", jobs.shape)
print("Skills shape:", skills_long.shape)

# ----------------------------------
# 1. Jobs dashboard file
# ----------------------------------

jobs_dashboard_cols = [
    "job_id",
    "company_id",
    "title",
    "role_category",
    "location",
    "formatted_work_type",
    "work_type",
    "remote_status_clean",
    "formatted_experience_level",
    "min_salary",
    "max_salary",
    "med_salary",
    "avg_salary",
    "pay_period",
    "currency",
    "technical_skill_count",
    "views",
    "applies",
    "sponsored",
    "description"
]

available_cols = [col for col in jobs_dashboard_cols if col in jobs.columns]

jobs_dashboard = jobs[available_cols].copy()

# Fill missing categories
jobs_dashboard["formatted_experience_level"] = jobs_dashboard["formatted_experience_level"].fillna("Not Specified")
jobs_dashboard["pay_period"] = jobs_dashboard["pay_period"].fillna("Not Specified")
jobs_dashboard["currency"] = jobs_dashboard["currency"].fillna("Not Specified")

jobs_dashboard.to_csv(PROCESSED_DATA_PATH / "jobs_dashboard.csv", index=False)

# ----------------------------------
# 2. Skills dashboard file
# ----------------------------------

skills_dashboard = skills_long.copy()

skills_dashboard.to_csv(PROCESSED_DATA_PATH / "skills_dashboard.csv", index=False)

# ----------------------------------
# 3. Skill summary
# ----------------------------------

skill_summary = (
    skills_long
    .groupby("technical_skill")
    .agg(
        job_count=("job_id", "nunique")
    )
    .reset_index()
    .sort_values("job_count", ascending=False)
)

skill_summary.to_csv(PROCESSED_DATA_PATH / "skill_summary_dashboard.csv", index=False)

# ----------------------------------
# 4. Skills by role summary
# ----------------------------------

skills_by_role = (
    skills_long
    .groupby(["role_category", "technical_skill"])
    .agg(
        job_count=("job_id", "nunique")
    )
    .reset_index()
    .sort_values(["role_category", "job_count"], ascending=[True, False])
)

skills_by_role.to_csv(PROCESSED_DATA_PATH / "skills_by_role_dashboard.csv", index=False)

# ----------------------------------
# 5. Role summary
# ----------------------------------

role_summary = (
    jobs
    .groupby("role_category")
    .agg(
        total_jobs=("job_id", "nunique"),
        avg_salary=("avg_salary", "mean"),
        jobs_with_salary=("avg_salary", lambda x: x.notnull().sum()),
        avg_skill_count=("technical_skill_count", "mean")
    )
    .reset_index()
    .sort_values("total_jobs", ascending=False)
)

role_summary.to_csv(PROCESSED_DATA_PATH / "role_summary_dashboard.csv", index=False)

# ----------------------------------
# 6. Remote work summary
# ----------------------------------

remote_summary = (
    jobs
    .groupby("remote_status_clean")
    .agg(
        total_jobs=("job_id", "nunique"),
        avg_salary=("avg_salary", "mean")
    )
    .reset_index()
    .sort_values("total_jobs", ascending=False)
)

remote_summary.to_csv(PROCESSED_DATA_PATH / "remote_summary_dashboard.csv", index=False)

# ----------------------------------
# 7. Salary dashboard
# ----------------------------------

salary_dashboard = jobs[
    jobs["avg_salary"].notnull()
][
    [
        "job_id",
        "title",
        "role_category",
        "location",
        "min_salary",
        "max_salary",
        "med_salary",
        "avg_salary",
        "pay_period",
        "currency"
    ]
].copy()

salary_dashboard.to_csv(PROCESSED_DATA_PATH / "salary_dashboard.csv", index=False)

# ----------------------------------
# Print summaries
# ----------------------------------

print("\nDashboard files created successfully!")

print("\nFiles saved:")
print(PROCESSED_DATA_PATH / "jobs_dashboard.csv")
print(PROCESSED_DATA_PATH / "skills_dashboard.csv")
print(PROCESSED_DATA_PATH / "skill_summary_dashboard.csv")
print(PROCESSED_DATA_PATH / "skills_by_role_dashboard.csv")
print(PROCESSED_DATA_PATH / "role_summary_dashboard.csv")
print(PROCESSED_DATA_PATH / "remote_summary_dashboard.csv")
print(PROCESSED_DATA_PATH / "salary_dashboard.csv")

print("\nSkill summary preview:")
print(skill_summary.head(15))

print("\nRole summary preview:")
print(role_summary)

print("\nRemote summary preview:")
print(remote_summary)

print("\nSalary dashboard shape:")
print(salary_dashboard.shape)