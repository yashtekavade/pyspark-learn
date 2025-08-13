from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('StructuredStreaming').getOrCreate()
df = spark.readStream.format('csv').option('header', 'true').load('data/stream_input')
df.writeStream.format('console').start().awaitTermination()
