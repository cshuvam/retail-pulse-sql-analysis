-- ============================================
-- Query 14: High Value Orders
-- Business Question: Which orders had a total
--   value exceeding ₹10,000?
-- ============================================

SELECT
    o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    c.city,
    SUM(oi.total_price) AS order_total
FROM
    orders o
    INNER JOIN order_items oi ON o.order_id = oi.order_id
    INNER JOIN customers c ON o.customer_id = c.customer_id
WHERE
    o.status = 'Completed'
GROUP BY
    o.order_id, o.order_date,
    c.first_name, c.last_name, c.city
HAVING
    SUM(oi.total_price) > 10000
ORDER BY
    order_total DESC;
