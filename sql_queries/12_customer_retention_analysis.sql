-- ============================================
-- Query 12: Customer Retention Analysis
-- Business Question: How many customers returned
--   to place another order within 90 days of
--   their first order?
-- ============================================

-- ── MySQL Version ──
WITH first_orders AS (
    -- Find each customer's first completed order date
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM
        orders
    WHERE
        status = 'Completed'
    GROUP BY
        customer_id
),
returning_customers AS (
    -- Find customers who ordered again within 90 days
    SELECT DISTINCT
        fo.customer_id
    FROM
        first_orders fo
        INNER JOIN orders o ON fo.customer_id = o.customer_id
    WHERE
        o.status = 'Completed'
        AND o.order_date > fo.first_order_date
        AND DATEDIFF(o.order_date, fo.first_order_date) <= 90
)
SELECT
    (SELECT COUNT(*) FROM first_orders) AS total_customers_with_orders,
    COUNT(*) AS retained_within_90_days,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM first_orders), 2
    ) AS retention_rate_pct
FROM
    returning_customers;

-- ── MS SQL Server Version ──
-- Change DATEDIFF line to:
-- AND DATEDIFF(DAY, fo.first_order_date, o.order_date) <= 90
