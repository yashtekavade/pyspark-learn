# PySpark Structured Streaming

Structured Streaming lets you process real-time data streams using DataFrames and SQL.

## 1. Streaming DataFrames
Create DataFrames from streaming sources (e.g., files, Kafka).
```python
df = spark.readStream.format('csv').option('header', 'true').load('data/stream_input')
```

## 2. Reading and Writing Streams
Read from a source and write to a sink (console, file, etc.).
```python
query = df.writeStream.format('console').start()
query.awaitTermination()
```

## 3. Window Operations
Aggregate data over time windows.
```python
from pyspark.sql.functions import window
df_windowed = df.groupBy(window(df['timestamp'], '10 minutes')).count()
```

## 4. Triggers
Control how often streaming queries are processed.
```python
query = df.writeStream.trigger(processingTime='1 minute').format('console').start()
```

---
See `streaming_example.py` for more code samples.
