import pandas as pd

df = pd.read_csv("superstore.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
import pandas as pd

df = pd.read_csv("superstore.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

print(df.head())
df['month']=df['Order Date'].dt.month
monthly_sales=df.groupby('month')['Sales'].sum()
print(monthly_sales)
import matplotlib.pyplot as plt

monthly_sales.plot(kind='line', marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
plt.savefig("C:/Users/YourName/Desktop/Project/graph.png")
