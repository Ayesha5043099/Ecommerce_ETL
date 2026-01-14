import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:ayesha123@localhost:5432/ecommerce")

customers_df = pd.read_sql("SELECT * FROM customers", engine)
products_df  = pd.read_sql("SELECT * FROM products", engine)
orders_df    = pd.read_sql("SELECT * FROM orders", engine)

customers_df.to_csv("data/raw/customers.csv", index=False)
products_df.to_csv("data/raw/products.csv", index=False)
orders_df.to_csv("data/raw/orders.csv", index=False)

print(" Data Extracted Successfully")
