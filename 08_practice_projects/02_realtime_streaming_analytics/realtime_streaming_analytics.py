"""
Real-Time Analytics with Streaming
Step-by-step code with explanations.
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# 1. Create SparkSession
spark = SparkSession.builder.appName('RealTime Streaming Analytics').getOrCreate()  # Entry point for PySpark

# 2. Read streaming data from a folder
stream_df = spark.readStream.format('csv').option('header', 'true').schema('user STRING, value INT').load('data/stream_input')  # Reads streaming CSV

# 3. Calculate running total per user
agg_stream_df = stream_df.groupBy('user').agg({'value': 'sum'}).withColumnRenamed('sum(value)', 'running_total')  # Aggregates values per user

# 4. Output results to console
query = agg_stream_df.writeStream.outputMode('complete').format('console').start()  # Writes output to console

# 5. Await termination
query.awaitTermination()  # Keeps the stream running
