import pandas as pd
import sqlite3

# ===== CONFIG =====
DATA_PATH = "../data/sample_data.csv"
DB_PATH = "../database/erp.db"

# ===== LOAD DATA =====
df = pd.read_csv(DATA_PATH)

# ===== DATA CLEANING =====
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df["order_date"] = pd.to_datetime(df["order_date"])

# ===== KPI CALCULATIONS =====
total_orders = len(df)
delayed_orders = df[df['status'] == 'Delayed'].shape[0]
delay_rate = (delayed_orders / total_orders) * 100
avg_delivery_days = df['delivery_days'].mean()

# Inventory risk
low_stock_count = df[df['inventory_level'] < 50].shape[0]

# ===== BUSINESS AGGREGATIONS =====

# Region performance
region_performance = df.groupby("region").agg({
    "delivery_days": "mean",
    "order_quantity": "sum"
}).reset_index()

# Product demand
category_demand = df.groupby("product_category").agg({
    "order_quantity": "sum"
}).reset_index()

# Supplier performance
supplier_performance = df.groupby("supplier").agg({
    "delivery_days": "mean"
}).reset_index()

# ===== ANOMALY DETECTION (simple rule-based) =====
# Mark high delay orders
df["delay_flag"] = df["delivery_days"].apply(lambda x: 1 if x > 7 else 0)

# ===== DATABASE STORAGE =====
conn = sqlite3.connect(DB_PATH)

# Store raw + processed data
df.to_sql("orders", conn, if_exists="replace", index=False)
region_performance.to_sql("region_performance", conn, if_exists="replace", index=False)
category_demand.to_sql("category_demand", conn, if_exists="replace", index=False)
supplier_performance.to_sql("supplier_performance", conn, if_exists="replace", index=False)

# KPI summary table
kpi_summary = pd.DataFrame({
    "total_orders": [total_orders],
    "delayed_orders": [delayed_orders],
    "delay_rate": [round(delay_rate, 2)],
    "avg_delivery_days": [round(avg_delivery_days, 2)],
    "low_stock_count": [low_stock_count]
})

kpi_summary.to_sql("kpi_summary", conn, if_exists="replace", index=False)

conn.close()

# ===== LOG OUTPUT =====
print("✅ Data pipeline executed successfully")
print(f"Total Orders: {total_orders}")
print(f"Delay Rate: {round(delay_rate, 2)}%")
print(f"Avg Delivery Days: {round(avg_delivery_days, 2)}")
print(f"Low Inventory Cases: {low_stock_count}")