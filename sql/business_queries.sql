-- Total Revenue

SELECT
ROUND(SUM(payment_value)::numeric,2)
AS total_revenue
FROM payments;


-- Monthly Revenue

SELECT
DATE_TRUNC(
    'month',
    CAST(order_purchase_timestamp AS TIMESTAMP)
) AS month,

ROUND(
    SUM(payment_value)::numeric,
    2
) AS revenue

FROM orders o

JOIN payments p
ON o.order_id = p.order_id

GROUP BY month

ORDER BY month;


-- Top States by Revenue

SELECT
c.customer_state,

ROUND(
    SUM(p.payment_value)::numeric,
    2
) AS revenue

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

JOIN payments p
ON o.order_id = p.order_id

GROUP BY c.customer_state

ORDER BY revenue DESC

LIMIT 10;


-- Order Status Analysis

SELECT
order_status,
COUNT(*) AS total_orders

FROM orders

GROUP BY order_status

ORDER BY total_orders DESC;


-- Top Customers

SELECT
c.customer_unique_id,

ROUND(
    SUM(p.payment_value)::numeric,
    2
) AS total_spent

FROM customers c

JOIN orders o
ON c.customer_id = o.customer_id

JOIN payments p
ON o.order_id = p.order_id

GROUP BY c.customer_unique_id

ORDER BY total_spent DESC

LIMIT 10;