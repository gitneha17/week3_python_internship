# Week 3 Internship Project
# NumPy and Pandas for Data Cleaning and Analysis
# Intern: Neha Beldar

import pandas as pd
import numpy as np

# Load dataset
file_path = "data/sales_data.csv"
df = pd.read_csv(file_path)

print("\n========== ORIGINAL DATASET ==========\n")
print(df)

# ----------------------------
# Data Cleaning
# ----------------------------

# Remove missing values
df_clean = df.dropna()

# Remove duplicate rows
df_clean = df_clean.drop_duplicates()

print("\n========== CLEANED DATASET ==========\n")
print(df_clean)

# ----------------------------
# NumPy Operations
# ----------------------------

sales_array = np.array(df_clean["Sales"])

print("\n========== NUMPY SALES ARRAY ==========")
print(sales_array)

print("\n========== SALES STATISTICS ==========")

print("Average Sales:", np.mean(sales_array))
print("Maximum Sales:", np.max(sales_array))
print("Minimum Sales:", np.min(sales_array))
print("Total Sales:", np.sum(sales_array))

# ----------------------------
# Pandas Data Analysis
# ----------------------------

print("\n========== SALES BY CATEGORY ==========")

category_sales = df_clean.groupby("Category")["Sales"].mean()

print(category_sales)

print("\n========== PRODUCT SALES SUMMARY ==========")

product_sales = df_clean.groupby("Product")["Sales"].sum()

print(product_sales)

print("\nData Analysis Completed Successfully!")