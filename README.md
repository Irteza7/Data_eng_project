# Weather Data Pipeline

This project is a data pipeline that fetches weather data, publishes it to a Kafka topic, consumes it, and stores it in a PostgreSQL database. The pipeline is orchestrated using Apache Airflow, and data analysis can be performed using Metabase.

The services used in this project are containerized using Docker and orchestrated using Docker Compose.


## Documentation

For a detailed description of the project, please refer to the [PROJECT REPORT](REPORT.md).


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

To set up the project, follow these steps:

1. Ensure Docker and Docker Compose are installed on your machine.

2. Clone the repository and navigate to the project directory.

3. Build the weather project package:

    ```bash
    cd weather_project
    python setup.py bdist_wheel
    cd ..
    ```

4. Create a `.env` file in the project directory and fill it with your own values. You can use `.env.example` as a template.

5. Create a `config.ini` file in the `utils` directory and fill it with your own values. You can use `config.ini.example` as a template.

6. Run the following command to start the services:

    ```bash
    docker-compose up -d --build
    ```

After following these steps, you should be able to access the Airflow webserver at `localhost:8080` and Metabase at `localhost:3000`.


## Running the Pipeline

After setting up the services, you can start the pipeline by triggering the Airflow DAG.

## Troubleshooting

If you face any issues while setting up or running the project, please check the service logs using the `docker logs <service_name>` command.

