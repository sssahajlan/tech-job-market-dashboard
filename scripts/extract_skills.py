import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")
CLEANED_DATA_PATH = Path("data/cleaned")
CLEANED_DATA_PATH.mkdir(parents=True, exist_ok=True)

# Load cleaned tech jobs and raw job skills
tech_jobs = pd.read_csv(CLEANED_DATA_PATH / "filtered_tech_jobs.csv")
job_skills = pd.read_csv(RAW_DATA_PATH / "job_skills.csv")

print("Files loaded successfully!")

print("\nTech jobs shape:")
print(tech_jobs.shape)

print("\nJob skills shape:")
print(job_skills.shape)

print("\nJob skills columns:")
print(job_skills.columns.tolist())

# Join skills to filtered tech jobs
tech_job_skills = tech_jobs[["job_id", "title", "role_category"]].merge(
    job_skills,
    on="job_id",
    how="left"
)

print("\nJoined tech job skills shape:")
print(tech_job_skills.shape)

print("\nPreview:")
print(tech_job_skills.head(20))

print("\nTop skills overall:")
print(tech_job_skills["skill_abr"].value_counts().head(20))

print("\nTop skills by role category:")
top_skills_by_role = (
    tech_job_skills
    .dropna(subset=["skill_abr"])
    .groupby(["role_category", "skill_abr"])
    .size()
    .reset_index(name="skill_count")
    .sort_values(["role_category", "skill_count"], ascending=[True, False])
)

print(top_skills_by_role.head(50))

# Save output
tech_job_skills.to_csv(CLEANED_DATA_PATH / "tech_job_skills.csv", index=False)
top_skills_by_role.to_csv(CLEANED_DATA_PATH / "top_skills_by_role.csv", index=False)

print("\nSaved files:")
print(CLEANED_DATA_PATH / "tech_job_skills.csv")
print(CLEANED_DATA_PATH / "top_skills_by_role.csv")