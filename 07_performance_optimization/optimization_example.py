from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark = SparkSession.builder.appName('Optimization').getOrCreate()
df_large = spark.read.csv('data/large.csv', header=True, inferSchema=True)
df_small = spark.read.csv('data/small.csv', header=True, inferSchema=True)
df_joined = df_large.join(broadcast(df_small), 'id')
df_joined.cache()
