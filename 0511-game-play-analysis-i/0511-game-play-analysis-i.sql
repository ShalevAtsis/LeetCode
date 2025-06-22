# Write your MySQL query statement below
SELECT player_id, 
    MIN(event_date) AS first_login
FROM Activity a
GROUP BY player_id;