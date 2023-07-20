# Weather Data Pipeline

This project is a data pipeline that fetches weather data, publishes it to a Kafka topic, consumes it, and stores it in a PostgreSQL database. The pipeline is orchestrated using Apache Airflow, and data analysis can be performed using Metabase.

The services used in this project are containerized using Docker and orchestrated using Docker Compose.

## Project Structure

The project is structured as follows:
```
.
├── docker-compose.yml
├── Dockerfile
├── services
│ └── airflow
│  └── dags
│   └── weather_dag.py
└── weather_project
├── consume_n_store.py
├── fetch_n_publish.py
└── utils
 ├── api_call.py
 ├── config.ini
 ├── kafka_init.py
 ├── postgres.py
 ├── settings.py
 └── util.py
```

- The `docker-compose.yml` file defines the services that make up the app.
- The `Dockerfile` is used to build the Airflow service.
- The `services` directory contains the service-specific files and directories.
- The `weather_project` directory contains the Python scripts for fetching, publishing, consuming, and storing weather data.
- The `utils` directory contains utility scripts and configuration files.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository.
2. Create a `.env` file in the project root and set the necessary environment variables. Refer to `.env.example` for the required variables.
3. Run `docker-compose up -d --build`.

The services should now be up and running. You can access the Airflow webserver at `http://localhost:8080` and Metabase at `http://localhost:3000`.

## Running the Pipeline

After setting up the services, you can start the pipeline by triggering the Airflow DAG.

## Troubleshooting

If you face any issues while setting up or running the project, please check the service logs using the `docker logs <service_name>` command.

## Documentation

For a detailed description of the project, please refer to the [PROJECT REPORT](REPORT.md).

