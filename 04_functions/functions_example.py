from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, udf
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName('Functions').getOrCreate()
df = spark.read.csv('data/input.csv', header=True, inferSchema=True)

def age_category(age):
    return 'adult' if age >= 18 else 'minor'

age_category_udf = udf(age_category)
df = df.withColumn('category', age_category_udf(col('age')))
