-- ============================================
-- Query 01: Find Total Sales
-- Business Question: What is the total revenue
--   generated from all completed orders?
-- ============================================

SELECT
    SUM(oi.total_price) AS total_revenue
FROM
    order_items oi
    INNER JOIN orders o ON oi.order_id = o.order_id
WHERE
    o.status = 'Completed';
