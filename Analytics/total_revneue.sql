SELECT 
    SUM(quantity * price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id;
