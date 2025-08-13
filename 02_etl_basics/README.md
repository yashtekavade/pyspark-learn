# PySpark ETL & Data Engineering Basics

This section explains how to use PySpark for ETL and basic data engineering tasks, with code examples for each concept.

## 1. SparkSession
SparkSession is the entry point to programming Spark with the Dataset and DataFrame API. It allows you to create DataFrames, read data, and manage Spark configurations.

**Code Example:**
```python
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
	.appName('ETL Example') \
	.getOrCreate()
```

## 2. Reading Data (CSV, Parquet, JSON)
PySpark can read data from various formats. Here is how to read a CSV file:

```python
df = spark.read.csv('data/input.csv', header=True, inferSchema=True)
```
Similarly, you can read Parquet and JSON:
```python
df_parquet = spark.read.parquet('data/input.parquet')
df_json = spark.read.json('data/input.json')
```

## 3. Writing Data
You can write DataFrames to different formats:
```python
df.write.parquet('data/output.parquet')
df.write.csv('data/output.csv', header=True)
df.write.json('data/output.json')
```

## 4. DataFrame Basics
DataFrames are distributed collections of data organized into named columns. You can perform operations like select, filter, and show:
```python
df.select('name', 'age').show()
df.filter(df['age'] > 18).show()
```

## 5. Schema Definition
You can define a schema explicitly for better control:
```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
	StructField('name', StringType(), True),
	StructField('age', IntegerType(), True)
])
df = spark.read.csv('data/input.csv', header=True, schema=schema)
```

## 6. Data Cleaning
Common cleaning operations include dropping nulls and removing duplicates:
```python
df_clean = df.dropna()
df_nodup = df_clean.dropDuplicates()
```

---

See `etl_example.py` for a complete sample ETL script.
