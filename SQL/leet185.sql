/*
LeetCode #185: Department Highest Salary
Code by Timothy Payne Jr.
Started on: July 28, 2021
Finished on: July 28, 2021
*/

SELECT Department, Employee, Salary
FROM(
SELECT Department.Name as Department,
Employee.Name as Employee,
Salary,
DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS sal_rank FROM Employee
LEFT JOIN Department ON
Department.Id = Employee.DepartmentId) sq
WHERE sal_rank <= 3;