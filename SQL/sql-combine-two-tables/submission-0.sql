-- Write your query below
SELECT first_name,last_name, city, state 
FROM address FULL JOIN person 
ON address.person_id = person.person_id where first_name IS NOT NULL AND last_name IS NOT NULL
