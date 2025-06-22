# Write your MySQL query statement below

SELECT total.Day, 
    IFNULL(ROUND(cancelled.Cancelled_trips / total.Total_trips, 2), 0) AS "Cancellation Rate"
FROM (    
    SELECT t.request_at AS 'Day',
        COUNT(*) AS Total_trips
    FROM trips AS t
    JOIN Users AS d ON t.driver_id = d.users_id AND d.role = 'driver'
    JOIN Users AS c ON t.client_id = c.users_id AND c.role = 'client'
    WHERE d.banned = 'No' 
    AND c.banned = 'No' 
    AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    GROUP BY t.request_at
) AS total
LEFT JOIN (
    SELECT t.request_at AS 'Day',
        COUNT(*) AS Cancelled_trips
    FROM trips AS t
    JOIN Users AS d ON t.driver_id = d.users_id AND d.role = 'driver'
    JOIN Users AS c ON t.client_id = c.users_id AND c.role = 'client'
    WHERE t.status LIKE 'cancelled%'
        AND d.banned = 'No'
        AND c.banned = 'No' 
        AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'

    GROUP BY t.request_at
) AS cancelled
ON total.Day = cancelled.Day
ORDER BY total.day;