# PySpark Functions

Learn about built-in and user-defined functions (UDFs) in PySpark.

## Topics
- Built-in functions (e.g., col, lit, when)
- User Defined Functions (UDFs)
- Applying functions to DataFrames

## Example
See `functions_example.py` for sample code.

---

PySpark provides many built-in functions for data manipulation, and you can also create your own User Defined Functions (UDFs).

## 1. Built-in Functions
- **col**: Refers to a column.
- **lit**: Creates a literal value.
- **when**: Conditional logic.
```python
from pyspark.sql.functions import col, lit, when
df = df.withColumn('is_adult', when(col('age') >= 18, lit('yes')).otherwise(lit('no')))
```

## 2. User Defined Functions (UDFs)
Create custom functions for complex logic.
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def age_group(age):
	return 'adult' if age >= 18 else 'minor'

age_group_udf = udf(age_group, StringType())
df = df.withColumn('group', age_group_udf(col('age')))
```

## 3. Applying Functions
You can use functions in select, withColumn, filter, etc.
```python
df.select(col('name'), (col('age') + 5).alias('age_plus_5')).show()
```

---
See `functions_example.py` for more code samples.
