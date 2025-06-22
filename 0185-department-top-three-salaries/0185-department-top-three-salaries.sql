# Write your MySQL query statement below

SELECT
    d.name AS Department,
    e1.name AS Employee,
    e1.salary AS Salary
FROM Employee AS e1
JOIN Department AS d ON e1.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee AS e2
    WHERE e1.departmentId = e2.departmentId
        AND e1.salary < e2.salary
) < 3;
