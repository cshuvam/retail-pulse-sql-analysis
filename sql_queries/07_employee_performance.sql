-- ============================================
-- Query 07: Employee Performance
-- Business Question: Which sales representatives
--   handled the most revenue?
-- ============================================

SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    e.role,
    COUNT(DISTINCT o.order_id) AS orders_handled,
    SUM(oi.total_price) AS total_revenue_handled
FROM
    employees e
    INNER JOIN orders o ON e.employee_id = o.employee_id
    INNER JOIN order_items oi ON o.order_id = oi.order_id
WHERE
    o.status = 'Completed'
GROUP BY
    e.employee_id, e.first_name, e.last_name, e.role
ORDER BY
    total_revenue_handled DESC;
