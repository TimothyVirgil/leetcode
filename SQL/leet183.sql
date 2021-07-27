/*
LeetCode #183: Customers Who Never Order
Code by Timothy Payne Jr.
Started on: July 27, 2021
Finished on: July 27, 2021
*/

SELECT Name AS Customers FROM Customers
LEFT OUTER JOIN Orders
ON Customers.Id = Orders.CustomerId
WHERE CustomerId IS NULL
