-- ============================================
-- Query 10: Products Never Purchased
-- Business Question: Which products in the
-- ============================================

SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.price,
    p.stock_quantity
FROM
    products p
    LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE
    oi.item_id IS NULL
ORDER BY
    p.category, p.product_name;
