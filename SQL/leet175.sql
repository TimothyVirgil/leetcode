/*
LeetCode #175: Combine Two Tables
Code by Timothy Payne Jr.
Started on: July 20, 2021
Finished on: July 20, 2021
*/

SELECT Firstname, LastName, Address.City, Address.State FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId;