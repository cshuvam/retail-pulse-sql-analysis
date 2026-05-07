-- ============================================
-- Query 11: Average Order Value
-- Business Question: What is the average value
-- ============================================

-- Using a CTE to first calculate each order's total,
-- then averaging across all orders
WITH order_values AS (
    SELECT
        o.order_id,
        SUM(oi.total_price) AS order_total
    FROM
        orders o
        INNER JOIN order_items oi ON o.order_id = oi.order_id
    WHERE
        o.status = 'Completed'
    GROUP BY
        o.order_id
)
SELECT
    COUNT(order_id) AS total_orders,
    ROUND(AVG(order_total), 2) AS avg_order_value,
    MIN(order_total) AS min_order_value,
    MAX(order_total) AS max_order_value
FROM
    order_values;
