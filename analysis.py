import pandas as pd
import matplotlib.pyplot as plt

# Sample Sales Dataset
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile",
                "Tablet", "Laptop", "Mobile"],
    "Sales": [55000, 25000, 18000, 60000, 30000, 20000, 65000, 28000],
    "Quantity": [2, 3, 2, 3, 4, 3, 2, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("SALES DATASET")
print(df)

# Data Analysis
print("\nDATASET SUMMARY")
print(df.describe())

# Total Sales
df["Revenue"] = df["Sales"] * df["Quantity"]
print("\nTOTAL REVENUE:", df["Revenue"].sum())

# Product-wise Analysis
print("\nPRODUCT WISE REVENUE")
print(df.groupby("Product")["Revenue"].sum())

# Save analyzed data
df.to_csv("sales_analysis.csv", index=False)

# Create Sales Ch…
[11:39 am, 26/11/2026] Taimoor Pasha: import pandas as pd
import matplotlib.pyplot as plt

# Sample Sales Dataset
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile",
                "Tablet", "Laptop", "Mobile"],
    "Sales": [55000, 25000, 18000, 60000, 30000, 20000, 65000, 28000],
    "Quantity": [2, 3, 2, 3, 4, 3, 2, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("SALES DATASET")
print(df)

# Data Analysis
print("\nDATASET SUMMARY")
print(df.describe())

# Total Sales
df["Revenue"] = df["Sales"] * df["Quantity"]
print("\nTOTAL REVENUE:", df["Revenue"].sum())

# Product-wise Analysis
print("\nPRODUCT WISE REVENUE")
print(df.groupby("Product")["Revenue"].sum())

# Save analyzed data
df.to_csv("sales_analysis.csv", index=False)

# Create Sales Chart
df.groupby("Product")["Revenue"].sum().plot(
    kind="bar",
    title="Product Wise Sales Analysis"
)

plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
print("\nAnalysis completed successfully!")

print("\nAnalysis completed successfully!")
