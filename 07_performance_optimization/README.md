# PySpark Performance Optimization

Optimize your PySpark jobs for speed and efficiency.

## 1. Caching and Persistence
Store intermediate results in memory for faster access.
```python
df.cache()
df.persist()
```

## 2. Partitioning
Control data distribution for better performance.
```python
df_repartitioned = df.repartition(10)
```

## 3. Broadcast Joins
Efficiently join large and small DataFrames.
```python
from pyspark.sql.functions import broadcast
df_joined = df_large.join(broadcast(df_small), 'id')
```

## 4. Avoiding Shuffles
Minimize expensive data movement by careful use of groupBy, join, etc.

## 5. Tuning Spark Configurations
Set Spark parameters for optimal performance.
```python
spark.conf.set('spark.sql.shuffle.partitions', 50)
```

---
See `optimization_example.py` for more code samples.
