customers
- customer_id (PK)

orders
- order_id (PK)
- customer_id (FK)

payments
- order_id (FK)

order_items
- order_id (FK)
- product_id (FK)

products
- product_id (PK)