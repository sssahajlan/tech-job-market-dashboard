# Tech Job Market Intelligence Dashboard Final Report

## Project Overview
This project analyzed LinkedIn job postings to identify trends in entry-level technology and data roles. The analysis focused on job categories, requested skills, salary trends, and remote work indicators.

## Dataset
The original dataset contained 15,886 job postings. After filtering for non-senior tech and data roles, the final analysis used 296 job postings.

## Tools Used
Python, Pandas, Regex, PostgreSQL, SQL, SQLAlchemy, Power BI, Git, and GitHub.

## Data Cleaning Process
The data was loaded from multiple CSV files, filtered for relevant roles, and cleaned for dashboard analysis. Senior, manager, director, lead, and executive-level roles were excluded to focus on entry-level and early-career positions.

## Skill Extraction
Technical and workplace skills were extracted from job descriptions using regex keyword matching. The final skill analysis identified 1,087 job-skill relationships across 270 jobs.

## Key Findings
- Software Engineering and Business Analyst / BI were the most common role categories.
- SQL, Database, Python, Java, Data Visualization, Excel, Statistics, JavaScript, AWS, and Git were among the most requested skills.
- 110 of the filtered job postings contained usable salary data.
- Remote and hybrid indicators appeared across multiple role categories, but many postings did not clearly specify remote status.

## Limitations
The dataset was filtered from a broader LinkedIn job posting dataset and may not represent the entire job market. Salary analysis includes both hourly and yearly pay periods, so pay period filtering is important when interpreting salary trends.

## Conclusion
This project demonstrates an end-to-end data analytics workflow, including data cleaning, skill extraction, SQL analysis, database loading, and dashboard development in Power BI.