-- ============================================
-- Query 09: Rank Top Customers
-- Business Question: Who are the top 5
--   customers by total spending?
-- ============================================

WITH customer_spending AS (
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        c.city,
        SUM(oi.total_price) AS total_spent,
        DENSE_RANK() OVER (
            ORDER BY SUM(oi.total_price) DESC
        ) AS spending_rank
    FROM
        customers c
        INNER JOIN orders o ON c.customer_id = o.customer_id
        INNER JOIN order_items oi ON o.order_id = oi.order_id
    WHERE
        o.status = 'Completed'
    GROUP BY
        c.customer_id, c.first_name, c.last_name, c.city
)
SELECT
    spending_rank,
    customer_id,
    first_name,
    last_name,
    city,
    total_spent
FROM
    customer_spending
WHERE
    spending_rank <= 5
ORDER BY
    spending_rank;
