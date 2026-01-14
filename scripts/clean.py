import pandas as pd

customers = pd.read_csv("data/raw/customers.csv")
orders = pd.read_csv("data/raw/orders.csv")

customers.drop_duplicates(inplace=True)
customers.dropna(subset=["customer_id", "email"], inplace=True)

orders["order_date"] = pd.to_datetime(orders["order_date"])
orders = orders[orders["quantity"] > 0]

customers.to_csv("data/processed/customers_clean.csv", index=False)
orders.to_csv("data/processed/orders_clean.csv", index=False)

print(" Data Cleaned")
