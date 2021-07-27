/*
LeetCode #182: Duplicate Emails
Code by Timothy Payne Jr.
Started on: July 27, 2021
Finished on: July 27, 2021
*/

SELECT Email FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;