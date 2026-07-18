import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Dataset .csv")
print(df.head())
print(df.shape)
print("Row =", df.shape[0])
print("Column =",df.shape[1])
print(df.columns)
print(df.info())
df = df.dropna()
print(df.isnull().sum())
print(df.shape)
print(df.dtypes)

print(df["Aggregate rating"].value_counts())

plt.figure(figsize=(8,5))
sns.histplot(df["Aggregate rating"],bins=20)
plt.title("Distribution of Aggregate Rating")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.show()
