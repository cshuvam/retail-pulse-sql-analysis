-- ============================================
-- Query 02: Top Selling Products
-- Business Question: Which are the top 10
--   best-selling products by quantity sold?
-- ============================================

-- ── MySQL Version ──
SELECT
    p.product_name,
    p.category,
    SUM(oi.quantity) AS total_qty_sold,
    SUM(oi.total_price) AS total_revenue
FROM
    order_items oi
    INNER JOIN products p ON oi.product_id = p.product_id
    INNER JOIN orders o ON oi.order_id = o.order_id
WHERE
    o.status = 'Completed'
GROUP BY
    p.product_name, p.category
ORDER BY
    total_qty_sold DESC
LIMIT 10;

-- ── MS SQL Server Version ──
-- SELECT TOP 10
--     p.product_name,
--     p.category,
--     SUM(oi.quantity) AS total_qty_sold,
--     SUM(oi.total_price) AS total_revenue
-- FROM
--     order_items oi
--     INNER JOIN products p ON oi.product_id = p.product_id
--     INNER JOIN orders o ON oi.order_id = o.order_id
-- WHERE
--     o.status = 'Completed'
-- GROUP BY
--     p.product_name, p.category
-- ORDER BY
--     total_qty_sold DESC;
