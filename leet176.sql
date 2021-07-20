/*
LeetCode #176: Combine Two Tables
Code by Timothy Payne Jr.
Started on: July 20, 2021
Finished on: July 20, 2021
*/

SELECT
IF((SELECT COUNT(Salary) FROM Employee) <= 1, NULL, 
	(SELECT DISTINCT Salary
      FROM Employee
      ORDER BY Salary DESC
      LIMIT 1 OFFSET 1))
      
AS SecondHighestSalary