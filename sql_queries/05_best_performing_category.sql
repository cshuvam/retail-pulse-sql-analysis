-- ============================================
-- Query 05: Best Performing Category
-- Business Question: Which product category
--   generates the highest revenue?
-- ============================================

SELECT
    p.category,
    COUNT(DISTINCT oi.item_id) AS items_sold,
    SUM(oi.quantity) AS total_qty,
    SUM(oi.total_price) AS category_revenue
FROM
    order_items oi
    INNER JOIN products p ON oi.product_id = p.product_id
    INNER JOIN orders o ON oi.order_id = o.order_id
WHERE
    o.status = 'Completed'
GROUP BY
    p.category
ORDER BY
    category_revenue DESC;
