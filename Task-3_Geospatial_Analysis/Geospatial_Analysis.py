import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Dataset .csv")
print(df.head())
print(df[["Latitude", "Longitude"]].head())

plt.figure(figsize=(10,6))
sns.scatterplot(x="Longitude", y="Latitude", data=df, alpha=0.6)
plt.title("Restaurant Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="Latitude", y="Aggregate rating", data=df)
plt.title("Aggregate Rating vs Latitude")
plt.xlabel("Latitude")
plt.ylabel("Aggregate Rating")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="Longitude", y="Aggregate rating", data=df)
plt.title("Aggregate Rating vs Longitude")
plt.xlabel("Longitude")
plt.ylabel("Aggregate Rating")
plt.tight_layout()
plt.show()
