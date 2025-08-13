# Project 2: Real-Time Streaming Analytics

This project shows how to use PySpark Structured Streaming for real-time analytics.

## Steps Explained

1. **Create SparkSession**
   - Entry point for PySpark streaming jobs.
2. **Read Streaming Data**
   - Reads streaming CSV data from a folder using `readStream`.
   - Schema is defined inline for simplicity.
3. **Calculate Running Total**
   - Aggregates the `value` column per user to get a running total.
4. **Output to Console**
   - Writes the results to the console in real time.
5. **Await Termination**
   - Keeps the streaming query running until stopped.

See `realtime_streaming_analytics.py` for the full code with line-by-line comments.
