import pandas as pd
from sqlalchemy import create_engine
engine = create_engine(
    "postgresql+psycopg2://postgres:das21077@localhost:5432/ecommerce_analytics"
)
customers = pd.read_csv(
    r"D:\Projects\autonomous-data-analyst\data\olist_customers_dataset.csv"
)

orders = pd.read_csv(
    r"D:\Projects\autonomous-data-analyst\data\olist_orders_dataset.csv"
)

products = pd.read_csv(
    r"D:\Projects\autonomous-data-analyst\data\olist_products_dataset.csv"
)

payments = pd.read_csv(
    r"D:\Projects\autonomous-data-analyst\data\olist_order_payments_dataset.csv"
)

items = pd.read_csv(
    r"D:\Projects\autonomous-data-analyst\data\olist_order_items_dataset.csv"
)

order_reviews = pd.read_csv(
    r"D:\Projects\autonomous-data-analyst\data\olist_order_reviews_dataset.csv"
)   

sellers = pd.read_csv(
    r"D:\Projects\autonomous-data-analyst\data\olist_sellers_dataset.csv"
)       

category_translation = pd.read_csv(
    r"D:\Projects\autonomous-data-analyst\data\product_category_name_translation.csv"
)   

customers.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

orders.to_sql(
    "orders",
    engine,
    if_exists="replace",
    index=False
)

products.to_sql(
    "products",
    engine,
    if_exists="replace",
    index=False
)

payments.to_sql(
    "payments",
    engine,
    if_exists="replace",
    index=False
)

items.to_sql(
    "order_items",
    engine,
    if_exists="replace",
    index=False
)

order_reviews.to_sql(
    "order_reviews",
    engine,
    if_exists="replace",
    index=False
)

sellers.to_sql(
    "sellers",
    engine,
    if_exists="replace",
    index=False
)

category_translation.to_sql(
    "category_translation",
    engine,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully!")