-- ============================================
-- Query 06: Repeat Customers
-- Business Question: How many customers have
-- ============================================

-- Total count of repeat customers
SELECT
    COUNT(*) AS repeat_customer_count
FROM (
    SELECT
        customer_id
    FROM
        orders
    WHERE
        status = 'Completed'
    GROUP BY
        customer_id
    HAVING
        COUNT(order_id) > 1
) AS repeat_cust;

-- Detailed list of repeat customers with order counts
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.city,
    COUNT(o.order_id) AS order_count
FROM
    customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
WHERE
    o.status = 'Completed'
GROUP BY
    c.customer_id, c.first_name, c.last_name, c.city
HAVING
    COUNT(o.order_id) > 1
ORDER BY
    order_count DESC;
