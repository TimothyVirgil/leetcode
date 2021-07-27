/*
LeetCode #178: Rank Scores
Code by Timothy Payne Jr.
Started on: July 26, 2021
Finished on: July 27, 2021

It took me a very long time to find that the DENSE_RANK function exists.
*/
SELECT Score AS score, 
DENSE_RANK() OVER(ORDER BY Score DESC) AS 'Rank' 
FROM Scores