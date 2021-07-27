/*
LeetCode #181: Employees Earning More Than Their Managers
Code by Timothy Payne Jr.
Started on: July 27, 2021
Finished on: July 27, 2021
*/

SELECT e2.Name AS 'Employee' FROM
Employee e1,
Employee e2
WHERE e1.Id = e2.ManagerId AND e2.Salary > e1.Salary;