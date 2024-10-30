
# Data Streaming to Cassandra

## Project Overview
This project demonstrates how to stream data from Kafka to Cassandra using Apache Spark and Docker. It involves creating a Kafka topic, producing messages, and consuming those messages to store them in a Cassandra database.

## Technologies Used
- Apache Kafka
- Apache Spark
- Cassandra
- Docker
- Apache Airflow

## Project Architecture
![Project Architecture](images/project_architecture.png)

## Services
The following services are included in this project:
- **Kafka**: A distributed messaging system used for sending messages between applications.
- **Cassandra**: A NoSQL database that stores the streamed data.
- **Spark**: A unified analytics engine for big data processing.
- **Airflow**: A platform to programmatically author, schedule, and monitor workflows. The fetching of data and streaming using the broker is managed inside an Apache Airflow DAG.

![Apache Airflow DAG](images/airflow.png)

## Running the Project
1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Build and start services using Docker Compose**:
    ```bash
    docker-compose up --build
    ```

3. **Access the services**:
    - Kafka: `localhost:9092`
    - Cassandra: `localhost:9042`
    - Airflow: `localhost:8080` (default username: `admin`, password: `admin`)

4. **Produce messages to Kafka**:
   You can use the Kafka console producer to send messages to the topic `users_created`.

5. **Monitor the streaming**:
   The application will read data from the Kafka topic using the jupyter notebook [spark_stream_cassandra.ipynb] and stream it into the Cassandra table `created_users`.

## Images
- **Data in Cassandra**: ![Data in Cassandra](images/data_in_cassandra.png)
- **Jobs**: ![Jobs](images/jobs.png)
- **Message Coming to Topics**: ![Message Coming to Topics](images/message_coming_to_topics.png)
- **Streaming to Cassandra**: ![Streaming to Cassandra](images/streaming_to_cassandra.png)

## Conclusion
This project illustrates the integration of Kafka, Spark, and Cassandra for real-time data processing, as well as the orchestration of the workflow using Apache Airflow.
