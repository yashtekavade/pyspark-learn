"""
Data Transformation and Aggregation Project
Step-by-step code with explanations.
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# 1. Create SparkSession
spark = SparkSession.builder.appName('Data Transformation Aggregation').getOrCreate()  # Entry point for PySpark

# 2. Read customer and transaction data
customer_df = spark.read.csv('data/customers.csv', header=True, inferSchema=True)  # Reads customer data
transaction_df = spark.read.csv('data/transactions.csv', header=True, inferSchema=True)  # Reads transaction data

# 3. Join customer and transaction data on customer_id
joined_df = customer_df.join(transaction_df, customer_df['customer_id'] == transaction_df['customer_id'], 'inner')  # Joins on customer_id

# 4. Calculate average spend per customer
avg_spend_df = joined_df.groupBy('customer_id').agg(avg('amount').alias('avg_spend'))  # Aggregates average spend

# 5. Show results
avg_spend_df.show()  # Displays average spend per customer
