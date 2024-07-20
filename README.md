# Realtime-Data-Streaming-Engine

The project is designed with the following components:

Data Source: We use randomuser.me API to generate random user data for our pipeline.
Apache Airflow: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
Apache Kafka and Zookeeper: Used for streaming data from PostgreSQL to the processing engine.
Control Center and Schema Registry: Helps in monitoring and schema management of our Kafka streams.
Apache Spark: For data processing with its master and worker nodes.
Cassandra: Where the processed data will be stored.


Architecture of the project:

https://github.com/airscholar/e2e-data-engineering/blob/main/Data%20engineering%20architecture.png
