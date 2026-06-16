import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales.csv")

monthly_sales = data.groupby("Month")["Sales"].sum()

print(monthly_sales)

monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
