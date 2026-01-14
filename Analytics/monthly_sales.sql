SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM(quantity * price) AS monthly_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY 1
ORDER BY 1;
