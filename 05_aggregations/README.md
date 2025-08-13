# PySpark Aggregations

Aggregations are used to summarize and analyze data in PySpark.

## 1. groupBy
Group data by one or more columns.
```python
df_grouped = df.groupBy('department')
```

## 2. agg
Apply aggregate functions like sum, avg, min, max.
```python
from pyspark.sql.functions import sum, avg
df_agg = df.groupBy('department').agg(sum('salary').alias('total_salary'), avg('salary').alias('avg_salary'))
```

## 3. pivot
Pivot data for better analysis.
```python
df_pivot = df.groupBy('year').pivot('department').sum('salary')
```

## 4. count, sum, avg, min, max
Basic aggregate functions.
```python
df_count = df.count()
df_sum = df.groupBy().sum('salary').collect()[0][0]
```

---
See `aggregations_example.py` for more code samples.
