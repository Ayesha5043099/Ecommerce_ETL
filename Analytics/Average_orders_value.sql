SELECT 
    AVG(order_total) AS avg_order_value
FROM (
    SELECT 
        order_id,
        SUM(quantity * price) AS order_total
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY order_id
) t;
