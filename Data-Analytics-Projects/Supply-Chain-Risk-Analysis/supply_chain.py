import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("supply_chain.csv")

high_risk = data[data["DelayDays"] > 5]

print("High Risk Deliveries")
print(high_risk)

plt.bar(data["Supplier"], data["DelayDays"])
plt.title("Supplier Delay Analysis")
plt.xlabel("Supplier")
plt.ylabel("Delay Days")
plt.show()
