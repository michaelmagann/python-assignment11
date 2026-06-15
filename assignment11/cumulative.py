import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT
    o.order_id,
    SUM(p.price * li.quantity) AS total_price
FROM orders o
JOIN line_items li
    ON o.order_id = li.order_id
JOIN products p
    ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""

df = pd.read_sql_query(query, conn)

print(df.head())

df["cumulative"] = df["total_price"].cumsum()

print("\nWith cumulative revenue:")
print(df.head())

df.plot(
    x="order_id",
    y="cumulative",
    kind="line",
    figsize=(10, 6)
)

plt.title("Cumulative Revenue Over Time")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.grid(True)

plt.show()

conn.close()