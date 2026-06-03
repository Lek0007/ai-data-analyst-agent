# Database Schema Documentation

## Overview

This database contains e-commerce transactional data from the Olist marketplace. The schema includes customer, order, product, payment, seller, review, and category information used for business analytics and AI-powered Text-to-SQL querying.

---

# Table: customers

## Primary Key

* customer_id

## Columns

| Column                   | Description                                          |
| ------------------------ | ---------------------------------------------------- |
| customer_id              | Unique identifier for a customer record              |
| customer_unique_id       | Unique customer identifier across multiple purchases |
| customer_zip_code_prefix | Customer ZIP code prefix                             |
| customer_city            | Customer city                                        |
| customer_state           | Customer state                                       |

## Relationships

* customers.customer_id → orders.customer_id

---

# Table: orders

## Primary Key

* order_id

## Foreign Keys

* customer_id → customers.customer_id

## Columns

| Column                        | Description                               |
| ----------------------------- | ----------------------------------------- |
| order_id                      | Unique order identifier                   |
| customer_id                   | Customer who placed the order             |
| order_status                  | Current status of the order               |
| order_purchase_timestamp      | Date and time when order was placed       |
| order_approved_at             | Date and time when payment was approved   |
| order_delivered_carrier_date  | Date when order was handed to carrier     |
| order_delivered_customer_date | Date when order was delivered to customer |
| order_estimated_delivery_date | Estimated delivery date                   |

## Relationships

* orders.customer_id → customers.customer_id
* orders.order_id → payments.order_id
* orders.order_id → order_items.order_id
* orders.order_id → order_reviews.order_id

---

# Table: products

## Primary Key

* product_id

## Columns

| Column                     | Description                   |
| -------------------------- | ----------------------------- |
| product_id                 | Unique product identifier     |
| product_category_name      | Product category              |
| product_name_lenght        | Length of product name        |
| product_description_lenght | Length of product description |
| product_photos_qty         | Number of product photos      |
| product_weight_g           | Product weight in grams       |
| product_length_cm          | Product length in centimeters |
| product_height_cm          | Product height in centimeters |
| product_width_cm           | Product width in centimeters  |

## Relationships

* products.product_id → order_items.product_id
* products.product_category_name → category_translation.product_category_name

---

# Table: payments

## Foreign Keys

* order_id → orders.order_id

## Columns

| Column               | Description                 |
| -------------------- | --------------------------- |
| order_id             | Associated order identifier |
| payment_sequential   | Payment sequence number     |
| payment_type         | Payment method              |
| payment_installments | Number of installments      |
| payment_value        | Payment amount              |

## Relationships

* payments.order_id → orders.order_id

---

# Table: order_items

## Composite Key

(order_id, order_item_id)

## Foreign Keys

* order_id → orders.order_id
* product_id → products.product_id
* seller_id → sellers.seller_id

## Columns

| Column              | Description                  |
| ------------------- | ---------------------------- |
| order_id            | Associated order identifier  |
| order_item_id       | Item number within an order  |
| product_id          | Purchased product            |
| seller_id           | Seller providing the product |
| shipping_limit_date | Shipping deadline            |
| price               | Product price                |
| freight_value       | Shipping cost                |

## Relationships

* order_items.order_id → orders.order_id
* order_items.product_id → products.product_id
* order_items.seller_id → sellers.seller_id

---

# Table: order_reviews

## Primary Key

* review_id

## Foreign Keys

* order_id → orders.order_id

## Columns

| Column                  | Description               |
| ----------------------- | ------------------------- |
| review_id               | Unique review identifier  |
| order_id                | Reviewed order            |
| review_score            | Customer rating (1-5)     |
| review_comment_title    | Review title              |
| review_comment_message  | Review text               |
| review_creation_date    | Review creation date      |
| review_answer_timestamp | Review response timestamp |

## Relationships

* order_reviews.order_id → orders.order_id

---

# Table: sellers

## Primary Key

* seller_id

## Columns

| Column                 | Description              |
| ---------------------- | ------------------------ |
| seller_id              | Unique seller identifier |
| seller_zip_code_prefix | Seller ZIP code prefix   |
| seller_city            | Seller city              |
| seller_state           | Seller state             |

## Relationships

* sellers.seller_id → order_items.seller_id

---

# Table: category_translation

## Primary Key

* product_category_name

## Columns

| Column                        | Description                          |
| ----------------------------- | ------------------------------------ |
| product_category_name         | Original Portuguese category name    |
| product_category_name_english | English translation of category name |

## Relationships

* category_translation.product_category_name → products.product_category_name

---

# Entity Relationship Summary

customers
→ orders
→ payments

customers
→ orders
→ order_reviews

orders
→ order_items
→ products
→ category_translation

order_items
→ sellers

This schema supports:

* Revenue Analytics
* Customer Analytics
* Product Analytics
* Seller Analytics
* Customer Review Analytics
* AI-powered Text-to-SQL Querying
