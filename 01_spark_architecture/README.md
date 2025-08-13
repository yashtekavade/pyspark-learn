# Spark Architecture

Understand the core concepts of Apache Spark architecture.

## 1. What is Spark?
Apache Spark is an open-source distributed computing system for big data processing and analytics. It provides high-level APIs in Python, Java, Scala, and R.

## 2. Cluster Components
- **Driver**: The process that runs the main function and creates the SparkContext.
- **Executors**: Worker processes that run tasks and store data.
- **Cluster Manager**: Allocates resources (YARN, Mesos, Standalone, Kubernetes).

**Diagram:**
```
Driver <-> Cluster Manager <-> Executors
```

## 3. DAG (Directed Acyclic Graph)
Spark builds a DAG of stages for job execution. Each transformation creates a new node in the DAG.

## 4. Spark Execution Flow
1. User writes code using Spark APIs.
2. Spark builds a DAG of execution.
3. Tasks are scheduled and executed on executors.
4. Results are collected back to the driver.

## 5. Resource Management
Spark manages resources using cluster managers and can scale horizontally.

## Example: Creating a SparkSession
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Architecture Example').getOrCreate()
print(spark)
```

---
Add diagrams and notes for deeper understanding as you learn.
