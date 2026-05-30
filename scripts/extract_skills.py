import pandas as pd
from pathlib import Path
import re

CLEANED_DATA_PATH = Path("data/cleaned")
CLEANED_DATA_PATH.mkdir(parents=True, exist_ok=True)

# Load cleaned tech jobs
tech_jobs = pd.read_csv(CLEANED_DATA_PATH / "filtered_tech_jobs.csv")

print("Filtered tech jobs loaded successfully!")
print("Tech jobs shape:", tech_jobs.shape)

# ----------------------------------
# 1. Define technical skills to search for
# ----------------------------------

technical_skills = {
    "SQL": [r"\bsql\b", r"\bmysql\b", r"\bpostgresql\b", r"\bpostgres\b"],
    "Python": [r"\bpython\b"],
    "Excel": [r"\bexcel\b", r"\bmicrosoft excel\b", r"\bspreadsheets?\b"],
    "Tableau": [r"\btableau\b"],
    "Power BI": [r"\bpower bi\b", r"\bpowerbi\b"],
    "Java": [r"\bjava\b"],
    "JavaScript": [r"\bjavascript\b", r"\bjs\b"],
    "R": [r"\br programming\b", r"\br language\b", r"\b r \b"],
    "AWS": [r"\baws\b", r"\bamazon web services\b"],
    "Azure": [r"\bazure\b", r"\bmicrosoft azure\b"],
    "Google Cloud": [r"\bgoogle cloud\b", r"\bgcp\b"],
    "Snowflake": [r"\bsnowflake\b"],
    "Git": [r"\bgit\b", r"\bgithub\b", r"\bgitlab\b"],
    "Pandas": [r"\bpandas\b"],
    "NumPy": [r"\bnumpy\b"],
    "Machine Learning": [r"\bmachine learning\b", r"\bml\b"],
    "Statistics": [r"\bstatistics\b", r"\bstatistical\b"],
    "Data Visualization": [r"\bdata visualization\b", r"\bvisualization\b", r"\bdashboard\b", r"\bdashboards\b"],
    "ETL": [r"\betl\b", r"\bextract transform load\b"],
    "BigQuery": [r"\bbigquery\b", r"\bgoogle bigquery\b"],
    "Looker": [r"\blooker\b"],
    "SAS": [r"\bsas\b"],
    "SPSS": [r"\bspss\b"],
    "Alteryx": [r"\balteryx\b"],
    "PowerPoint": [r"\bpowerpoint\b"],
    "Communication": [r"\bcommunication\b", r"\bcommunicate\b"],
    "Problem Solving": [r"\bproblem solving\b", r"\banalytical skills\b"],
    "Data Cleaning": [r"\bdata cleaning\b", r"\bdata quality\b", r"\bclean data\b"],
    "Database": [r"\bdatabase\b", r"\bdatabases\b", r"\brelational database\b"]
}

# ----------------------------------
# 2. Function to extract skills
# ----------------------------------

def extract_technical_skills(description):
    description = str(description).lower()
    found_skills = []

    for skill, patterns in technical_skills.items():
        for pattern in patterns:
            if re.search(pattern, description):
                found_skills.append(skill)
                break

    return found_skills

tech_jobs["technical_skills"] = tech_jobs["description"].apply(extract_technical_skills)
tech_jobs["technical_skill_count"] = tech_jobs["technical_skills"].apply(len)

# ----------------------------------
# 3. Create one row per job-skill pair
# ----------------------------------

job_skill_rows = []

for _, row in tech_jobs.iterrows():
    job_id = row["job_id"]
    title = row["title"]
    role_category = row["role_category"]

    for skill in row["technical_skills"]:
        job_skill_rows.append({
            "job_id": job_id,
            "title": title,
            "role_category": role_category,
            "technical_skill": skill
        })

technical_skills_long = pd.DataFrame(job_skill_rows)

# ----------------------------------
# 4. Analyze top technical skills
# ----------------------------------

print("\nTechnical skill extraction complete!")

print("\nJobs with at least one technical skill:")
print((tech_jobs["technical_skill_count"] > 0).sum())

print("\nTop technical skills overall:")
print(technical_skills_long["technical_skill"].value_counts().head(30))

top_technical_skills_by_role = (
    technical_skills_long
    .groupby(["role_category", "technical_skill"])
    .size()
    .reset_index(name="skill_count")
    .sort_values(["role_category", "skill_count"], ascending=[True, False])
)

print("\nTop technical skills by role:")
print(top_technical_skills_by_role.head(80))

# ----------------------------------
# 5. Save outputs
# ----------------------------------

tech_jobs.to_csv(CLEANED_DATA_PATH / "filtered_tech_jobs_with_skills.csv", index=False)
technical_skills_long.to_csv(CLEANED_DATA_PATH / "technical_skills_long.csv", index=False)
top_technical_skills_by_role.to_csv(CLEANED_DATA_PATH / "top_technical_skills_by_role.csv", index=False)

print("\nSaved files:")
print(CLEANED_DATA_PATH / "filtered_tech_jobs_with_skills.csv")
print(CLEANED_DATA_PATH / "technical_skills_long.csv")
print(CLEANED_DATA_PATH / "top_technical_skills_by_role.csv")