/*
LeetCode #180: Consecutive Numbers
Code by Timothy Payne Jr.
Started on: July 27, 2021
Finished on: July 27, 2021
*/

SELECT DISTINCT(num) as ConsecutiveNums
FROM (SELECT logs.*,
	  (ROW_NUMBER() OVER (ORDER BY id) - 
       ROW_NUMBER() OVER (PARTITION BY num ORDER BY id))
	 AS grp FROM logs) logs
	 GROUP BY grp, num
	 HAVING COUNT(*) >= 3