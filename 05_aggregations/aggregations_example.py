from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, sum, count

spark = SparkSession.builder.appName('Aggregations').getOrCreate()
df = spark.read.csv('data/input.csv', header=True, inferSchema=True)
df_grouped = df.groupBy('department').agg(avg('salary').alias('avg_salary'), sum('salary').alias('total_salary'))
