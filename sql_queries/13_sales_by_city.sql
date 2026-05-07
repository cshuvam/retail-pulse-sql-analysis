-- ============================================
-- Query 13: Sales by City
-- Business Question: Which cities generate the
-- ============================================

SELECT
    c.city,
    c.state,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT c.customer_id) AS unique_customers,
    SUM(oi.total_price) AS city_revenue
FROM
    customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    INNER JOIN order_items oi ON o.order_id = oi.order_id
WHERE
    o.status = 'Completed'
GROUP BY
    c.city, c.state
ORDER BY
    city_revenue DESC;
