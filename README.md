📊 Week 3 – NumPy and Pandas for Data Manipulation
📌 Internship Task

This project is part of my Python Data Analysis Internship – Week 3.
The focus of this task is to learn and apply NumPy and Pandas libraries for data manipulation, data cleaning, and basic data analysis.

NumPy is used for numerical operations and array processing, while Pandas is used for handling structured datasets such as CSV files.

🎯 Project Objective

The objective of this task is to:

Understand NumPy arrays and mathematical operations

Learn Pandas DataFrame operations

Perform data cleaning and preprocessing

Analyze sales data using aggregation and grouping techniques

🛠 Technologies Used

Python

NumPy

Pandas

VS Code

📂 Project Structure
week3_numpy_pandas_internship
│
├── data
│   └── sales_data.csv
│
├── data_analysis_project.py
│
├── README.md
│
└── Week3_Internship_Report.docx
📊 Dataset Description

The dataset sales_data.csv contains information about product sales.

Column	Description
Product	Name of the product
Category	Category of the product
Sales	Sales amount

The dataset includes:

Duplicate records

Missing values

These issues are handled during the data cleaning process.

🧹 Data Cleaning Steps

The Python script performs the following operations:

Load Dataset
The dataset is loaded using Pandas.

Remove Missing Values
Rows containing missing values are removed.

Remove Duplicate Records
Duplicate rows are removed to ensure accurate data.

Prepare Data for Analysis
Cleaned data is used for further analysis.

🔢 NumPy Operations

NumPy is used for performing numerical analysis on the sales data.

The following statistics are calculated:

Average Sales

Maximum Sales

Minimum Sales

Total Sales

These calculations demonstrate the use of NumPy arrays and mathematical operations.

📈 Data Analysis with Pandas

Pandas is used to perform data aggregation and grouping.

Category-wise Sales Analysis

Average sales are calculated for each product category.

Product-wise Sales Summary

Total sales for each product are computed using groupby operations.

▶️ How to Run the Project

1️⃣ Install required libraries

pip install numpy pandas

2️⃣ Navigate to the project folder

cd week3_numpy_pandas_internship

3️⃣ Run the Python script

python data_analysis_project.py
🖥 Example Output
Average Sales: 20571
Maximum Sales: 55000
Minimum Sales: 5000
Total Sales: 144000

The program also displays category-wise and product-wise sales analysis.

📚 Concepts Learned

Through this project, I learned:

NumPy

NumPy arrays

Mathematical operations

Statistical calculations

Pandas

DataFrames

Reading CSV files

Data cleaning

Handling missing values

Removing duplicates

Data aggregation using groupby

📄 Internship Report

A detailed explanation of the project and concepts learned is available in:

Week3_Internship_Report.docx
👩‍💻 Author

Neha Beldar
Python Data Analysis Intern
