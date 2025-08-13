# Project 3: Data Transformation and Aggregation

This project demonstrates joining, transforming, and aggregating data using PySpark.

## Steps Explained

1. **Create SparkSession**
   - Entry point for all PySpark operations.
2. **Read Data**
   - Reads customer and transaction data from CSV files.
3. **Join Data**
   - Joins customer and transaction DataFrames on `customer_id`.
4. **Calculate Average Spend**
   - Groups by `customer_id` and calculates average transaction amount.
5. **Show Results**
   - Displays the average spend per customer.

See `data_transformation_aggregation.py` for the full code with line-by-line comments.
