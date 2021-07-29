/*
LeetCode #196: Delete Duplicate Emails
Code by Timothy Payne Jr.
Started on: July 29, 2021
Finished on: July 29, 2021
*/

/*I'd like to use a WITH clause but leetcode doesn't do CTE apparently
WITH dr AS
(SELECT DENSE_RANK() OVER (PARTITION BY Email ORDER BY Id) FROM Person)
DELETE FROM Person
WHERE dr > 1;
That's what I want but Leetcode will not allow.*/

DELETE PERSON FROM PERSON
JOIN (SELECT id, 
	DENSE_RANK() OVER(PARTITION BY Email ORDER BY Id) AS dr2 
	FROM Person) dr
ON PERSON.id = dr.id
WHERE dr.dr2 > 1;