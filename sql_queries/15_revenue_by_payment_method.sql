-- ============================================
-- Query 15: Revenue by Payment Method
-- Business Question: How does total revenue
--   break down by payment method?
-- ============================================

SELECT
    p.payment_method,
    COUNT(*) AS transaction_count,
    SUM(p.amount) AS total_revenue,
    ROUND(
        SUM(p.amount) * 100.0 /
        (SELECT SUM(amount) FROM payments
         INNER JOIN orders o2 ON payments.order_id = o2.order_id
         WHERE o2.status = 'Completed'),
        2
    ) AS revenue_share_pct
FROM
    payments p
    INNER JOIN orders o ON p.order_id = o.order_id
WHERE
    o.status = 'Completed'
GROUP BY
    p.payment_method
ORDER BY
    total_revenue DESC;
