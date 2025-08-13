from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName('Transformations').getOrCreate()
df = spark.read.csv('data/input.csv', header=True, inferSchema=True)
df_filtered = df.filter(col('age') > 18)
df_selected = df_filtered.select('name', 'age')
