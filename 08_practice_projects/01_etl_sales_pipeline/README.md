# Project 1: ETL Pipeline for Sales Data

This project demonstrates a simple ETL pipeline using PySpark to process sales data.

## Steps Explained

1. **Create SparkSession**
   - Entry point for PySpark. Required for all operations.
   - `spark = SparkSession.builder.appName('ETL Sales Pipeline').getOrCreate()`
2. **Define Schema**
   - Explicitly defines the structure of the sales data for better control.
   - Uses `StructType` and `StructField`.
3. **Read Data**
   - Reads sales data from a CSV file using the defined schema.
   - `spark.read.csv('data/sales.csv', header=True, schema=schema)`
4. **Data Cleaning**
   - Removes rows with missing values using `dropna()`.
5. **Add Calculated Column**
   - Adds a new column `total_sales` by multiplying `units_sold` and `unit_price`.
6. **Aggregate Sales by Region**
   - Groups data by `region` and sums `total_sales` for each region.
7. **Write Results**
   - Saves the aggregated results to a Parquet file for efficient storage.
8. **Show Results**
   - Displays the final aggregated sales per region.

See `etl_sales_pipeline.py` for the full code with line-by-line comments.
