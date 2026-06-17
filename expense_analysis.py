import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("expenses.csv")

# Data Cleaning
df.dropna(inplace=True)

# Total Expense
total = df["Amount"].sum()
print("Total Expense:", total)

# Category-wise expense
category_expense = df.groupby("Category")["Amount"].sum()
print("\nCategory-wise Expense:\n", category_expense)

# Highest expense category
highest = category_expense.idxmax()
print("\nHighest Spending Category:", highest)

# Visualization - Pie Chart
plt.figure()
category_expense.plot(kind="pie", autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.ylabel("")
plt.savefig("pie_chart.png")

# Visualization - Bar Graph
plt.figure()
category_expense.plot(kind="bar")
plt.title("Category-wise Expense")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.savefig("bar_chart.png")

print("\nCharts saved successfully!")
