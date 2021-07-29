/*
LeetCode #196: Delete Duplicate Emails
Code by Timothy Payne Jr.
Started on: July 29, 2021
Finished on: July 29, 2021
This one is kind of a mess. It works. 
I am feeling very hamstrung by the inability to use CTE.
*/


SELECT w2id AS id FROM
( SELECT *, DATEDIFF(w2date,w1date) AS dd FROM
(SELECT w1.id AS 'w1id', 
 w1.recordDate AS 'w1date',
 w1.temperature AS 'w1temp',
 w2.id AS 'w2id',
 w2.recordDate as 'w2date',
 w2.Temperature as 'w2temp' FROM
Weather w1,
Weather w2) w ) b
WHERE dd = 1 AND (w2temp>w1temp)