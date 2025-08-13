# PySpark Transformations

Transformations are operations that produce a new DataFrame from an existing one. They are lazy and only executed when an action is called.

## 1. map (via RDD)
Used for element-wise operations on RDDs.
```python
rdd = spark.sparkContext.parallelize([1, 2, 3])
rdd2 = rdd.map(lambda x: x * 2)
print(rdd2.collect())
```

## 2. filter
Select rows based on a condition.
```python
df_filtered = df.filter(df['age'] > 18)
```

## 3. select
Choose specific columns.
```python
df_selected = df.select('name', 'age')
```

## 4. join
Combine two DataFrames based on a key.
```python
df_joined = df1.join(df2, df1.id == df2.id, 'inner')
```

## 5. withColumn
Add or update a column.
```python
from pyspark.sql.functions import col
df_new = df.withColumn('age_plus_10', col('age') + 10)
```

---
See `transformations_example.py` for more code samples.
