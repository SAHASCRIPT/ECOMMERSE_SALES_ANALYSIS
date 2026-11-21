import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ecommerce_sales.csv", parse_dates=["Order_Date"])
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

print("Total revenue:", df["Sales"].sum())
print("Total orders:", df["Order_ID"].nunique())
print("\nRevenue by product:\n", df.groupby("Product")["Sales"].sum().sort_values(ascending=False))
print("\nRevenue by city:\n", df.groupby("City")["Sales"].sum().sort_values(ascending=False))
print("\nPayment method counts:\n", df["Payment_Method"].value_counts())

df.groupby("Month")["Sales"].sum().plot(marker="o", title="Monthly Sales Trend")
plt.xlabel("Month"); plt.ylabel("Revenue"); plt.xticks(rotation=45)
plt.tight_layout(); plt.savefig("monthly_sales.png"); plt.show()

df.groupby("Product")["Sales"].sum().sort_values().plot(kind="barh", title="Revenue by Product")
plt.xlabel("Revenue"); plt.tight_layout(); plt.savefig("product_revenue.png"); plt.show()
