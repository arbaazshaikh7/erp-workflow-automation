import sqlite3

conn = sqlite3.connect("../database/erp.db")
df = conn.execute("SELECT * FROM kpi_summary").fetchall()

delay_rate = df[0][2]

if delay_rate > 30:
    print("ALERT: High delay rate detected!")

conn.close()