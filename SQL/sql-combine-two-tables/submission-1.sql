-- Write your query below
SELECT first_name,last_name, city, state 
FROM address  RIGHT JOIN person 
ON address.person_id = person.person_id;
