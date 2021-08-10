/*
LeetCode #595: Big Countries
Code by Timothy Payne Jr.
Started on: August 10, 2021
Finished on: August 10, 2021
*/

SELECT name, population, area FROM World
WHERE area > 3000000 OR population > 25000000;