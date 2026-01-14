import pandas as pd
import logging
import os
from sqlalchemy import create_engine, text

# ---------------- LOGGING ----------------
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/orders_etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- DB ----------------
DB_URL = "postgresql://postgres:ayesha123@localhost:5432/ecommerce"
engine = create_engine(DB_URL)

# ---------------- ETL ----------------
def load_orders():
    logging.info("Orders ETL started")

    csv_path = "data/raw/orders.csv"

    if not os.path.exists(csv_path):
        logging.error(f"File not found: {csv_path}")
        raise FileNotFoundError(csv_path)

    df = pd.read_csv(csv_path)

    # ✅ Drop price ONLY if exists
    if "price" in df.columns:
        df.drop(columns=["price"], inplace=True)

    # ✅ Remove duplicates already in DB
    with engine.connect() as conn:
        existing_ids = pd.read_sql(
            text("SELECT order_id FROM orders"),
            conn
        )

    df = df[~df["order_id"].isin(existing_ids["order_id"])]

    if df.empty:
        logging.info("No new orders to insert")
        print("No new orders to insert")
        return

    df.to_sql("orders", engine, if_exists="append", index=False)

    logging.info(f"Inserted {len(df)} rows into orders")
    print(f"Inserted {len(df)} rows into orders")

# ---------------- RUN ----------------
if __name__ == "__main__":
    load_orders()
