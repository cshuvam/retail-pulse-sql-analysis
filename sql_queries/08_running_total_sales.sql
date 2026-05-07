-- ============================================
-- Query 08: Running Total Sales
-- Business Question: What is the cumulative
-- ============================================

SELECT
    order_date,
    daily_revenue,
    SUM(daily_revenue) OVER (
        ORDER BY order_date
    ) AS running_total
FROM (
    -- First, calculate daily revenue
    SELECT
        o.order_date,
        SUM(oi.total_price) AS daily_revenue
    FROM
        orders o
        INNER JOIN order_items oi ON o.order_id = oi.order_id
    WHERE
        o.status = 'Completed'
    GROUP BY
        o.order_date
) AS daily_sales
ORDER BY
    order_date;
