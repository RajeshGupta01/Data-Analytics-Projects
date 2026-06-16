import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("weather.csv")

print("Average Temperature:", data["Temperature"].mean())

plt.plot(data["Date"], data["Temperature"])
plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.show()
