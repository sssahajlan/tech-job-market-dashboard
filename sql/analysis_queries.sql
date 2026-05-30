-- =====================================================
-- Tech Job Market Intelligence Dashboard
-- SQL Analysis Queries
-- =====================================================

-- 1. Total jobs analyzed
SELECT 
    COUNT(*) AS total_jobs
FROM jobs_dashboard;


-- 2. Job count by role category
SELECT 
    role_category,
    COUNT(*) AS total_jobs
FROM jobs_dashboard
GROUP BY role_category
ORDER BY total_jobs DESC;


-- 3. Top 10 most requested technical skills
SELECT 
    technical_skill,
    job_count
FROM skill_summary_dashboard
ORDER BY job_count DESC
LIMIT 10;


-- 4. Top skills by role category
SELECT 
    role_category,
    technical_skill,
    job_count
FROM skills_by_role_dashboard
ORDER BY role_category, job_count DESC;


-- 5. Average salary by role
SELECT 
    role_category,
    ROUND(AVG(avg_salary), 2) AS average_salary,
    COUNT(*) AS jobs_with_salary
FROM salary_dashboard
GROUP BY role_category
ORDER BY average_salary DESC;


-- 6. Remote work distribution
SELECT 
    remote_status_clean,
    total_jobs,
    ROUND(avg_salary, 2) AS average_salary
FROM remote_summary_dashboard
ORDER BY total_jobs DESC;


-- 7. Top roles by average number of skills requested
SELECT 
    role_category,
    total_jobs,
    ROUND(avg_skill_count, 2) AS average_skill_count
FROM role_summary_dashboard
ORDER BY average_skill_count DESC;


-- 8. Rank technical skills within each role category
SELECT
    role_category,
    technical_skill,
    job_count,
    RANK() OVER (
        PARTITION BY role_category 
        ORDER BY job_count DESC
    ) AS skill_rank
FROM skills_by_role_dashboard;


-- 9. Top 3 skills for each role category using CTE
WITH ranked_skills AS (
    SELECT
        role_category,
        technical_skill,
        job_count,
        RANK() OVER (
            PARTITION BY role_category 
            ORDER BY job_count DESC
        ) AS skill_rank
    FROM skills_by_role_dashboard
)
SELECT
    role_category,
    technical_skill,
    job_count,
    skill_rank
FROM ranked_skills
WHERE skill_rank <= 3
ORDER BY role_category, skill_rank;


-- 10. Jobs with the highest number of technical skills
SELECT
    title,
    role_category,
    location,
    technical_skill_count,
    remote_status_clean
FROM jobs_dashboard
ORDER BY technical_skill_count DESC
LIMIT 20;


-- 11. Salary comparison by remote status
SELECT
    remote_status_clean,
    COUNT(*) AS jobs_with_salary,
    ROUND(AVG(avg_salary), 2) AS average_salary,
    ROUND(MIN(avg_salary), 2) AS min_salary,
    ROUND(MAX(avg_salary), 2) AS max_salary
FROM salary_dashboard s
JOIN jobs_dashboard j
    ON s.job_id = j.job_id
GROUP BY remote_status_clean
ORDER BY average_salary DESC;


-- 12. Skills connected to Data Analyst roles
SELECT
    technical_skill,
    COUNT(DISTINCT job_id) AS job_count
FROM skills_dashboard
WHERE role_category = 'Data Analyst'
GROUP BY technical_skill
ORDER BY job_count DESC;


-- 13. Skills connected to Business Analyst / BI roles
SELECT
    technical_skill,
    COUNT(DISTINCT job_id) AS job_count
FROM skills_dashboard
WHERE role_category = 'Business Analyst / BI'
GROUP BY technical_skill
ORDER BY job_count DESC;


-- 14. Skills connected to Software Engineering roles
SELECT
    technical_skill,
    COUNT(DISTINCT job_id) AS job_count
FROM skills_dashboard
WHERE role_category = 'Software Engineering'
GROUP BY technical_skill
ORDER BY job_count DESC;


-- 15. High-demand skills appearing in at least 25 jobs
SELECT
    technical_skill,
    job_count
FROM skill_summary_dashboard
WHERE job_count >= 25
ORDER BY job_count DESC;