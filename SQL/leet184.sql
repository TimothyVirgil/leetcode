/*
LeetCode #184: Department Highest Salary
Code by Timothy Payne Jr.
Started on: July 27, 2021
Finished on: July 27, 2021
*/

SELECT Department, Employee, Salary
FROM
(SELECT Department.Name as Department, Employee.Name AS Employee, Salary, MAX(Salary)
OVER (PARTITION BY Department.Name ORDER BY Salary DESC) as 'max'
FROM Employee
JOIN Department ON
Employee.DepartmentId = Department.Id) sq
WHERE Salary = max