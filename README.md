# Tech Job Market Intelligence Dashboard

## Project Overview
This project analyzes entry-level technology and data job postings to identify skill demand, role trends, salary patterns, and remote work indicators. The goal is to help recent graduates understand which technical skills and job categories are most common in the current tech job market.

## Business Questions
- Which technical skills are most frequently requested in tech and data job postings?
- Which job categories appear most often?
- How do salary trends vary across role categories?
- How common are remote, hybrid, and on-site job postings?
- What skills appear most often for Data Analyst, Business Analyst, Software Engineering, and Data Science roles?

## Tools Used
- Python
- Pandas
- Regex
- PostgreSQL
- SQLAlchemy
- SQL
- Power BI
- Git/GitHub

## Dataset
The project uses a LinkedIn job postings dataset from Kaggle. The raw dataset included job postings, companies, job skills, job industries, and benefits files.

The original dataset contained 15,886 job postings. After filtering for non-senior technology and data-related roles, the final analysis focused on 296 relevant job postings.

## Project Workflow
1. Loaded raw CSV files using Python.
2. Filtered for relevant tech and data roles.
3. Removed senior, manager, director, lead, and executive-level roles.
4. Categorized jobs into role groups such as Software Engineering, Business Analyst / BI, Data Analyst, Data Science / ML, Developer, and Analytics.
5. Extracted technical skills from job descriptions using regex.
6. Created dashboard-ready CSV files.
7. Loaded processed files into PostgreSQL.
8. Wrote SQL queries using aggregations, CTEs, joins, and window functions.
9. Built an interactive Power BI dashboard.

## Key Results
- 296 non-senior tech/data jobs analyzed.
- 270 jobs contained at least one extracted technical skill.
- 1,087 job-skill relationships were identified.
- Top requested skills included SQL, Database, Python, Java, Data Visualization, Excel, Statistics, JavaScript, AWS, and Git.
- Software Engineering and Business Analyst / BI were the most common role categories.
- Salary data was available for 110 jobs.

## Dashboard Pages
The Power BI dashboard includes:
- Executive Summary
- Skills Analysis
- Salary Analysis
- Remote Work Analysis

## SQL Analysis
The SQL analysis includes:
- Total jobs analyzed
- Job counts by role category
- Top requested skills
- Average salary by role
- Remote work distribution
- Top skills by role using window functions
- Top 3 skills per role using CTEs

## Repository Structure
```text
data/
  cleaned/
  processed/
dashboard/
notebooks/
reports/
scripts/
sql/
README.md
requirements.txt