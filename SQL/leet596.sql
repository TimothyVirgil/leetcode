/*
LeetCode #596: Classes More Than 5 Students
Code by Timothy Payne Jr.
Started on: August 10, 2021
Finished on: August 10, 2021
*/


SELECT class FROM
(SELECT class, COUNT(DISTINCT(student)) AS class_size FROM courses
GROUP BY class) b
WHERE class_size >=5;