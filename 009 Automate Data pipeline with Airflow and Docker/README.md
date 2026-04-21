# Project 9: Automating Data Pipelines with Apache Airflow and Docker

This project demonstrates how to set up and run **Apache Airflow** inside Docker containers, orchestrate a simple data pipeline, and understand the basics of workflow automation. It's ideal for data engineers learning how to containerize and manage complex ETL/ELT workflows.

## Technologies Used

- **Docker** & **Docker Compose** – Containerization and service orchestration  
- **Apache Airflow** – Workflow scheduling and monitoring  
- **PostgreSQL** – Airflow metadata database  
- **Python** – DAG definition and custom operators  

## Prerequisites

- Docker Engine ≥ 20.10 and Docker Compose ≥ 2.0 (or Docker Desktop)  
- At least 4 GB of RAM allocated to Docker  
- Basic command-line knowledge  

## Project Structure
airflow-docker-project/
├── dags/ # Place your DAG Python files here
│ └── hello_world_dag.py # Sample DAG (provided below)
├── docker-compose.yml # Airflow + PostgreSQL services
└── README.md # This file

text

## Getting Started

1. Clone or Create the Project Folder
     `git clone https://github.com/abdiomari/Docker-Stuff-start.git`

2. Navigate to 009 Directory.  
3. Start the environment    
 `docker-compose up -d`   
4. Access the Airflow UI.  
Open your browser and go to http://localhost:8080. 
Log in with:   
    - username: admin
    - password: admin   

You should see the hello_airflow_pipeline DAG in the list. 

## What’s Next?
Now that you have a working Airflow + Docker environment, you can:

Add more Python functions to read/write to databases (PostgreSQL, MySQL), cloud storage (S3, GCS), or APIs.

Use Airflow operators: PostgresOperator, DockerOperator, EmailOperator, etc.

Schedule your DAG with cron expressions: schedule_interval='0 9 * * *' (daily at 9 AM).

Connect to external systems using Airflow Connections (set via UI or environment variables).

