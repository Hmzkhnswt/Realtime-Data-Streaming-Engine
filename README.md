# Realtime Data Streaming Engine

This project demonstrates a real-time data streaming engine using Apache Kafka, Apache Spark, Cassandra, and Airflow. The setup involves a series of Docker containers to create an environment for real-time data ingestion, processing, and storage.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Docker Setup](#docker-setup)
  - [Kafka Setup](#kafka-setup)
  - [Spark Setup](#spark-setup)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Docker
- Docker Compose
- Python 3.8 or higher
- Apache Kafka CLI tools (optional, for manual topic management)

## Setup

### Docker Setup

1. Clone the repository:

```sh
git clone https://github.com/yourusername/Realtime-Data-Streaming-Engine.git
cd Realtime-Data-Streaming-Engine
```

2. Build and start the Docker containers:

```sh
docker-compose up -d
```

This command will start the following services:
- Zookeeper
- Kafka Broker
- Kafka Schema Registry
- Kafka Control Center
- Airflow (Webserver, Scheduler, Postgres)
- Spark (Master and Worker)
- Cassandra

### Kafka Setup

1. Create Kafka topics:

```sh
docker exec -it broker kafka-topics --create --topic your_topic --bootstrap-server broker:9092 --partitions 1 --replication-factor 1
```

2. List all topics to verify:

```sh
docker exec -it broker kafka-topics --list --bootstrap-server broker:9092
```

### Spark Setup

Make sure you have the required dependencies. You can use Maven to download the dependencies or place the jar files directly into the `jars` directory.

```sh
spark-shell --packages com.datastax.spark:spark-cassandra-connector_2.13:3.5.0
```

## Running the Application

1. Start your Spark job:

```sh
python3 spark_stream.py
```

2. Monitor the Airflow web UI:

Open a web browser and go to `http://localhost:8080`. The default username and password are both `airflow`.

## Project Structure

```plaintext
.
├── dags/                       # Airflow DAGs
├── script/
│   └── entrypoint.sh           # Airflow entrypoint script
├── requirements.txt            # Python dependencies
├── spark_stream.py             # Spark streaming application
├── docker-compose.yml          # Docker Compose configuration
└── README.md                   # Project README
```

## Usage

1. **Data Ingestion**: Use Kafka producers to send data to the Kafka topic.
2. **Data Processing**: Spark will consume data from Kafka, process it, and store it in Cassandra.
3. **Monitoring**: Use the Kafka Control Center and Airflow web UI for monitoring and management.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
