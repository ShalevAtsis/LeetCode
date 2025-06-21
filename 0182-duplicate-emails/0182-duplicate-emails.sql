# Write your MySQL query statement below
SELECT email AS Email
FROM person
GROUP BY email
HAVING COUNT(*) > 1;
