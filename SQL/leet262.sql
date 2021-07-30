/*
LeetCode #262: Trips and Users
Code by Timothy Payne Jr.
Started on: July 30, 2021
Finished on: July 30, 2021
Could do this a lot cleaner in PostGres or with a few more queries in MYSQL
*/

SELECT tot_req.request_at AS Day, 
IFNULL(round(comp_req.comp_count/tot_req.tot_count,2),0) AS 'Cancellation Rate' FROM
(SELECT request_at, COUNT(status) AS comp_count FROM
(SELECT clients.*, users.banned as driver_ban FROM
(SELECT *, users.banned as client_ban FROM trips
JOIN users ON
trips.client_id = users.users_id WHERE
 request_at = '2013-10-01' OR request_at='2013-10-02' OR request_at = '2013-10-03'
) clients
JOIN users ON
clients.driver_id = users.users_id) d
WHERE driver_ban = 'No' AND client_ban = 'No' AND (status = 'cancelled_by_driver'
                                                   OR status = 'cancelled_by_client')
GROUP BY request_at) comp_req
LEFT JOIN
(SELECT request_at, COUNT(status) AS tot_count FROM
(SELECT clients.*, users.banned as driver_ban FROM
(SELECT *, users.banned as client_ban FROM trips
JOIN users ON
trips.client_id = users.users_id) clients
JOIN users ON
clients.driver_id = users.users_id) d
WHERE driver_ban = 'No' AND client_ban = 'No'
GROUP BY request_at) tot_req
ON tot_req.request_at = comp_req.request_at

UNION

SELECT tot_req.request_at AS Day, 
IFNULL(round(comp_req.comp_count/tot_req.tot_count,2),0) AS 'Cancellation Rate' FROM
(SELECT request_at, COUNT(status) AS comp_count FROM
(SELECT clients.*, users.banned as driver_ban FROM
(SELECT *, users.banned as client_ban FROM trips
JOIN users ON
trips.client_id = users.users_id
WHERE request_at = '2013-10-01' OR request_at='2013-10-02' OR request_at = '2013-10-03') clients
JOIN users ON
clients.driver_id = users.users_id) d
WHERE driver_ban = 'No' AND client_ban = 'No' AND (status = 'cancelled_by_driver'
                                                   OR status = 'cancelled_by_client')
GROUP BY request_at) comp_req
RIGHT JOIN
(SELECT request_at, COUNT(status) AS tot_count FROM
(SELECT clients.*, users.banned as driver_ban FROM
(SELECT *, users.banned as client_ban FROM trips
JOIN users ON
trips.client_id = users.users_id
 WHERE
request_at = '2013-10-01' OR request_at='2013-10-02' OR request_at = '2013-10-03') clients
JOIN users ON
clients.driver_id = users.users_id) d
WHERE driver_ban = 'No' AND client_ban = 'No'
GROUP BY request_at) tot_req
ON tot_req.request_at = comp_req.request_at
