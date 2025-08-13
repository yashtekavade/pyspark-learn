"""
ETL Pipeline for Sales Data
Step-by-step code with explanations.
"""
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# 1. Create SparkSession
spark = SparkSession.builder.appName('ETL Sales Pipeline').getOrCreate()  # Entry point for PySpark

# 2. Define schema for sales data
schema = StructType([
    StructField('region', StringType(), True),
    StructField('product', StringType(), True),
    StructField('units_sold', IntegerType(), True),
    StructField('unit_price', DoubleType(), True)
])

# 3. Read sales data from CSV
sales_df = spark.read.csv('data/sales.csv', header=True, schema=schema)  # Reads CSV with schema

# 4. Data cleaning: drop rows with nulls
sales_df_clean = sales_df.dropna()  # Removes rows with missing values

# 5. Add total_sales column
sales_df_clean = sales_df_clean.withColumn('total_sales', sales_df_clean['units_sold'] * sales_df_clean['unit_price'])  # Calculates total sales

# 6. Aggregate sales by region
agg_df = sales_df_clean.groupBy('region').sum('total_sales').withColumnRenamed('sum(total_sales)', 'region_total_sales')  # Sums sales per region

# 7. Write results to Parquet
agg_df.write.parquet('data/region_sales.parquet')  # Saves output as Parquet file

# 8. Show results
agg_df.show()  # Displays aggregated sales
