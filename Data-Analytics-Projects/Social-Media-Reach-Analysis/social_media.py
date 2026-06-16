import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("social_media.csv")

data["Engagement"] = (
    data["Likes"] +
    data["Comments"] +
    data["Shares"]
)

print(data[["PostID", "Engagement"]])

plt.bar(data["PostID"], data["Engagement"])
plt.title("Post Engagement Analysis")
plt.xlabel("Post ID")
plt.ylabel("Engagement")
plt.show()
