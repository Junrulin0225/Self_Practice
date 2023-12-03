SELECT * FROM public.immunizations


SELECT * 
FROM encounters
WHERE encounterclass IN ('inpatient','ambulatory')



SELECT description,
	COUNT(*) AS counst_of_cond
FROM PUBLIC.conditions
WHERE description != 'Body Mass Index 30.0-30.9, adult'
GROUP BY description
HAVING COUNT(*) > 5000
ORDER BY counst_of_cond DESC


SELECT * FROM patients
WHERE city = 'Boston'


SELECT *
FROM PUBLIC.conditions
WHERE code IN ('585.1', '585.2', '585.3', '585.4')


------------------
-- This query gives me the count of all patients
------------------
SELECT city, COUNT(city)
FROM patients
WHERE city != 'Boston'
GROUP BY city
HAVING count(city) >= 100
ORDER BY count desc



SELECT t2.first,
	t2.last,
	t2.birthdate,
	t1.*
	
FROM public.immunizations AS t1
LEFT JOIN public.patients AS t2
on t1.patient = t2.id

