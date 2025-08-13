# Spark Architecture

Understand the core concepts of Apache Spark architecture.

## 1. What is Spark?
Apache Spark is an open-source distributed computing system for big data processing and analytics. It provides high-level APIs in Python, Java, Scala, and R.

## 2. Cluster Components
- **Driver**: The process that runs the main function and creates the SparkContext.
- **Executors**: Worker processes that run tasks and store data.
- **Cluster Manager**: Allocates resources (YARN, Mesos, Standalone, Kubernetes).

**Diagram:**

<img width="626" height="296" alt="image" src="https://github.com/user-attachments/assets/859af517-46fb-4d9d-bbd8-c10ecb8b1f46" />

### 2.1 For additional learning on this topic, I would recommend reading the following.
- What is Spark Job
- What is the Spark Stage? Explained
- What is Spark Executor
- What is Apache Spark Driver?
- What is DAG in Spark or PySpark
- What is a Lineage Graph in Spark?
- How to Submit a Spark Job via Rest API?

## 3. DAG (Directed Acyclic Graph)
Spark builds a DAG of stages for job execution. Each transformation creates a new node in the DAG.

## 4. Spark Execution Flow
1. User writes code using Spark APIs.
2. Spark builds a DAG of execution.
3. Tasks are scheduled and executed on executors.
4. Results are collected back to the driver.

## 5. Resource Management
Spark manages resources using cluster managers and can scale horizontally.

### 5.1 spark-shell
Spark binary comes with an interactive spark-shell. In order to start a shell, go to your SPARK_HOME/bin directory and type “spark-shell“. This command loads the Spark and displays what version of Spark you are using.

<img width="606" height="274" alt="image" src="https://github.com/user-attachments/assets/c4214876-5a61-4678-9be6-0a9b2eb38c60" />

spark-shell

By default, spark-shell provides with spark (SparkSession) and sc (SparkContext) objects to use. Let’s see some examples.

<img width="598" height="304" alt="image" src="https://github.com/user-attachments/assets/189b4733-6de7-425c-b128-0506499e7650" />

spark-shell create RDD

Spark-shell also creates a Spark context web UI and by default, it can access from http://localhost:4041.


### 5.2 Spark-submit

The spark-submit command is a utility to run or submit a Spark or PySpark application program (or job) to the cluster by specifying options and configurations, the application you are submitting can be written in Scala, Java, or Python (PySpark) code. You can use this utility in order to do the following.

- Submitting Spark applications on different cluster managers like Yarn, Kubernetes, Mesos, and Stand-alone.
- Submitting Spark application on client or cluster deployment modes

```
./bin/spark-submit \
  --master <master-url> \
  --deploy-mode <deploy-mode> \
  --conf <key<=<value> \
  --driver-memory <value>g \
  --executor-memory <value>g \
  --executor-cores <number of cores>  \
  --jars  <comma separated dependencies>
  --class <main-class> \
  <application-jar> \
  [application-arguments]
```

### 5.3 Spark Web UI

Apache Spark provides a suite of Web UIs (Jobs, Stages, Tasks, Storage, Environment, Executors, and SQL) to monitor the status of your Spark application, resource consumption of the Spark cluster, and Spark configurations. On Spark Web UI, you can see how the operations are executed.

<img width="605" height="383" alt="image" src="https://github.com/user-attachments/assets/17af6de9-20c9-4b2e-83f6-5062da89e0f6" />


Spark Web UI

