import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")
CLEANED_DATA_PATH = Path("data/cleaned")
CLEANED_DATA_PATH.mkdir(parents=True, exist_ok=True)

job_postings = pd.read_csv(RAW_DATA_PATH / "job_postings.csv")
companies = pd.read_csv(RAW_DATA_PATH / "companies.csv")
job_skills = pd.read_csv(RAW_DATA_PATH / "job_skills.csv")
job_industries = pd.read_csv(RAW_DATA_PATH / "job_industries.csv")
benefits = pd.read_csv(RAW_DATA_PATH / "benefits.csv")

print("Files loaded successfully!")

target_keywords = [
    "data analyst",
    "business analyst",
    "software engineer",
    "software developer",
    "data scientist",
    "machine learning",
    "analytics",
    "business intelligence",
    "bi analyst",
    "database analyst",
    "junior developer",
    "entry level software",
    "entry-level software",
    "python developer",
    "sql developer",
    "java developer",
    "analytics analyst"
]

exclude_keywords = [
    "senior",
    "sr.",
    "sr ",
    "manager",
    "director",
    "lead",
    "principal",
    "staff",
    "head of",
    "vp",
    "vice president",
    "architect",
    "iii",
    "ii"
]


def is_target_role(title):
    title = str(title).lower()
    return any(keyword in title for keyword in target_keywords)

def is_not_senior_role(title):
    title = str(title).lower()
    return not any(keyword in title for keyword in exclude_keywords)

tech_jobs = job_postings[
    job_postings["title"].apply(is_target_role)
    & job_postings["title"].apply(is_not_senior_role)
].copy()

print("\nFiltered non-senior tech/data jobs shape:")
print(tech_jobs.shape)

print("\nTop filtered job titles:")
print(tech_jobs["title"].value_counts().head(30))

# -----------------------------
# 2. Create role categories
# -----------------------------

def categorize_role(title):
    title = str(title).lower()

    if "data analyst" in title:
        return "Data Analyst"
    elif "business analyst" in title or "business intelligence" in title or "bi analyst" in title:
        return "Business Analyst / BI"
    elif "data scientist" in title or "machine learning" in title:
        return "Data Science / ML"
    elif "software engineer" in title or "software developer" in title:
        return "Software Engineering"
    elif "python developer" in title or "java developer" in title or "sql developer" in title:
        return "Developer"
    elif "analytics" in title:
        return "Analytics"
    else:
        return "Other Tech/Data"

tech_jobs["role_category"] = tech_jobs["title"].apply(categorize_role)

print("\nRole category counts:")
print(tech_jobs["role_category"].value_counts())

# -----------------------------
# 3. Clean remote status
# -----------------------------

def categorize_remote(row):
    if row["remote_allowed"] == 1:
        return "Remote Allowed"

    formatted_work_type = str(row["formatted_work_type"]).lower()
    title = str(row["title"]).lower()
    description = str(row["description"]).lower()

    if "remote" in formatted_work_type or "remote" in title or "remote" in description:
        return "Remote Mentioned"
    elif "hybrid" in description or "hybrid" in formatted_work_type:
        return "Hybrid Mentioned"
    else:
        return "Not Specified / On-site"

tech_jobs["remote_status_clean"] = tech_jobs.apply(categorize_remote, axis=1)

print("\nRemote status counts:")
print(tech_jobs["remote_status_clean"].value_counts())

# -----------------------------
# 4. Clean salary columns
# -----------------------------

salary_cols = ["min_salary", "max_salary", "med_salary"]

for col in salary_cols:
    tech_jobs[col] = pd.to_numeric(tech_jobs[col], errors="coerce")

tech_jobs["avg_salary"] = tech_jobs[["min_salary", "max_salary"]].mean(axis=1)

print("\nSalary availability:")
print(tech_jobs[["min_salary", "max_salary", "med_salary", "avg_salary"]].notnull().sum())

# -----------------------------
# 5. Save cleaned filtered dataset
# -----------------------------

tech_jobs.to_csv(CLEANED_DATA_PATH / "filtered_tech_jobs.csv", index=False)

print("\nCleaned filtered tech jobs saved to:")
print(CLEANED_DATA_PATH / "filtered_tech_jobs.csv")