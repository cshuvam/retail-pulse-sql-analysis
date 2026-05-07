-- ============================================
-- Query 03: Customers With No Orders
-- Business Question: Which registered customers
--   have never placed an order?
-- ============================================

-- Method 1: LEFT JOIN + IS NULL
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    c.city
FROM
    customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE
    o.order_id IS NULL
ORDER BY
    c.customer_id;

-- Method 2: NOT EXISTS (alternative approach)
-- SELECT
--     c.customer_id,
--     c.first_name,
--     c.last_name,
--     c.email,
--     c.city
-- FROM
--     customers c
-- WHERE
--     NOT EXISTS (
--         SELECT 1
--         FROM orders o
--         WHERE o.customer_id = c.customer_id
--     )
-- ORDER BY
--     c.customer_id;
