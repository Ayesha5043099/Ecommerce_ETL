# Ecommerce_ETL

## Project Overview
This project is a **data engineering pipeline for an e-commerce platform**, designed to ingest, clean, store, and analyze data related to customers, products, and orders. The goal is to provide a structured and automated workflow that allows analysts and business stakeholders to query and analyze the data efficiently.

The project demonstrates the core concepts of **ETL (Extract, Transform, Load)**, **relational database design**, and **SQL-based analytics**, making it ideal for learning practical data engineering skills.

---

## Features
- Automated **data ingestion** from CSV files (customers, products, orders).  
- **Data cleaning and transformation** to ensure data consistency.  
- **Relational database schema** with primary and foreign keys:
  - `customers` table
  - `products` table
  - `orders` table
- SQL queries for **data analysis and reporting**.
- Modular **Python scripts** for pipeline automation.

---

## Project Structure
<img width="269" height="580" alt="image" src="https://github.com/user-attachments/assets/a9eceb02-0401-4fd7-b9e4-5cd5bce34daa" />


---

## Tools and Technologies
- **Python**: For data cleaning, transformation, and automation scripts.  
- **Pandas**: Data manipulation and preprocessing.  
- **PostgreSQL**: Relational database to store structured data.  
- **SQLAlchemy**: Python ORM for database connection and operations.  
- **pgAdmin**: GUI interface to query and manage PostgreSQL database.  
- **CSV files**: Source data format for customers, products, and orders.  

---
## How It Works

1. **Data Ingestion**:  
   CSV files are placed in the `data/raw/` folder.  

2. **Data Cleaning**:  
   Run `scripts/clean.py` to remove missing values, standardize formats, and create clean CSVs in `data/processed/`.

3. **Loading Data into PostgreSQL**:  
   - Connect to PostgreSQL using `src/db_connection.py`.  
   - Load each table using the corresponding script (`load_orders.py`).  
   - Foreign keys enforce relationships between orders, customers, and products.  

4. **Data Analytics**:  
   - Use **pgAdmin** or Python scripts to run SQL queries for business insights:
     - Total orders per customer
     - Revenue per product category
     - Customer activity trends
     - etc.

---
