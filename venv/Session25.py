import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("Citytemps.csv")
print(df)
print(df.head(5))
print(df.tail(5))


print(df["Amritsar"])
print(df.Amritsar)

plt.figure(figsize=(15,10))
sns.countplot(x="Month", data=df)
plt.show()