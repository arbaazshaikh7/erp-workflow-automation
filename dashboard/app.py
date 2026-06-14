import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("../database/erp.db")

orders = pd.read_sql("SELECT * FROM orders", conn)
kpi = pd.read_sql("SELECT * FROM kpi_summary", conn)

st.title("ERP Analytics Dashboard")

st.metric("Total Orders", int(kpi['total_orders'][0]))
st.metric("Delayed Orders", int(kpi['delayed_orders'][0]))
st.metric("Delay %", float(kpi['delay_rate'][0]))

st.bar_chart(orders['inventory_level'])

conn.close()