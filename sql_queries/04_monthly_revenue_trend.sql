-- ============================================
-- Query 04: Monthly Revenue Trend
-- Business Question: What is the revenue trend
--   month over month for 2025?
-- ============================================

-- ── MySQL Version ──
SELECT
    DATE_FORMAT(o.order_date, '%Y-%m') AS order_month,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.total_price) AS monthly_revenue
FROM
    orders o
    INNER JOIN order_items oi ON o.order_id = oi.order_id
WHERE
    o.status = 'Completed'
GROUP BY
    DATE_FORMAT(o.order_date, '%Y-%m')
ORDER BY
    order_month;

-- ── MS SQL Server Version ──
-- SELECT
--     FORMAT(o.order_date, 'yyyy-MM') AS order_month,
--     COUNT(DISTINCT o.order_id) AS total_orders,
--     SUM(oi.total_price) AS monthly_revenue
-- FROM
--     orders o
--     INNER JOIN order_items oi ON o.order_id = oi.order_id
-- WHERE
--     o.status = 'Completed'
-- GROUP BY
--     FORMAT(o.order_date, 'yyyy-MM')
-- ORDER BY
--     order_month;
