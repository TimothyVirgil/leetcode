/*
LeetCode #177: Combine Two Tables
Code by Timothy Payne Jr.
Started on: July 20, 2021
Finished on: July 20, 2021
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
 DECLARE X INT unsigned DEFAULT N-1;
  RETURN (     
      SELECT
        IF((SELECT COUNT(Salary) FROM Employee)<N, NULL, 
           (SELECT DISTINCT Salary
      FROM Employee
      ORDER BY Salary DESC
      LIMIT 1 OFFSET X))        
  );
END