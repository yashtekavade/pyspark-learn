from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('ETL Example').getOrCreate()
df = spark.read.csv('data/input.csv', header=True, inferSchema=True)
df_clean = df.dropna()
df_clean.write.parquet('data/output.parquet')
