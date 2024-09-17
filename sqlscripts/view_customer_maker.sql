CREATE VIEW successful_signee_view AS
SELECT s.first_name AS first_name, s.surname AS surname, sc.country AS country, s.dob AS date_of_birth, spi.industry AS industry, spi.job_title AS role
FROM signee s
JOIN signee_professional_information spi
ON spi.signee_id = s.id 
JOIN signee_country sc 
ON sc.signee_id = s.id
WHERE s.is_successful = 1;

CREATE VIEW rejected_signee_view AS
SELECT s.first_name AS first_name, s.surname AS surname, sc.country AS country, s.dob AS date_of_birth, spi.industry AS industry, spi.job_title AS role
FROM signee s
JOIN signee_professional_information spi
ON spi.signee_id = s.id 
JOIN signee_country sc 
ON sc.signee_id = s.id
WHERE s.is_successful = 0;