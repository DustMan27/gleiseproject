SELECT s.id, upper(s.first_name) AS first_name, upper(s.surname) as surname, upper(spi.industry) as industry, upper(spi.job_title) AS job_title, spi.salary, i.relevancy AS job_score, s.prs AS prs
FROM signee AS s
JOIN signee_professional_information AS spi
ON spi.signee_id = s.id
JOIN industry AS i
ON i.industry_name = spi.industry;
