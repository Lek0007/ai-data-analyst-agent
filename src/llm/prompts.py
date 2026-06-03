schema = """
Table: customers
Columns:
customer_id
customer_unique_id
customer_zip_code_prefix
customer_city
customer_state

Table: orders
Columns:
order_id
customer_id
order_status
order_purchase_timestamp
order_approved_at
order_delivered_carrier_date
order_delivered_customer_date
order_estimated_delivery_date

Table: payments
Columns:
order_id
payment_sequential
payment_type
payment_installments
payment_value

Table: products
Columns:
product_id
product_category_name
product_name_lenght
product_description_lenght
product_photos_qty
product_weight_g
product_length_cm
product_height_cm
product_width_cm

Table: sellers
Columns:
seller_id
seller_zip_code_prefix
seller_city
seller_state

Table: order_items
Columns:
order_id
order_item_id
product_id
seller_id
shipping_limit_date
price
freight_value

Table: order_reviews
Columns:
review_id
order_id
review_score
review_comment_title
review_comment_message
review_creation_date
review_answer_timestamp

Table: category_translation
Columns:
product_category_name
product_category_name_english
"""

relationships = """
Relationships:

customers.customer_id = orders.customer_id

orders.order_id = payments.order_id

orders.order_id = order_items.order_id

orders.order_id = order_reviews.order_id

order_items.product_id = products.product_id

order_items.seller_id = sellers.seller_id

products.product_category_name =
category_translation.product_category_name
"""

examples = """
Example 1

Question:
Show top states by revenue

SQL:
SELECT
c.customer_state,
SUM(p.payment_value) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id
GROUP BY c.customer_state
ORDER BY revenue DESC;


Example 2

Question:
Show monthly revenue

SQL:
SELECT
DATE_TRUNC(
    'month',
    CAST(o.order_purchase_timestamp AS TIMESTAMP)
) AS month,
SUM(p.payment_value) AS revenue
FROM orders o
JOIN payments p
ON o.order_id = p.order_id
GROUP BY month
ORDER BY month;


Example 3

Question:
Show top sellers by revenue

SQL:
SELECT
s.seller_id,
SUM(oi.price) AS revenue
FROM sellers s
JOIN order_items oi
ON s.seller_id = oi.seller_id
GROUP BY s.seller_id
ORDER BY revenue DESC;
"""