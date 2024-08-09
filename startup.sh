#!/bin/bash
# Inicializa o banco de dados do Airflow (necessário apenas uma vez, mas não é prejudicial se executado repetidamente)
airflow db init

# Inicia o Webserver na porta 8080
airflow webserver -p 8080 &

# Inicia o Scheduler
airflow scheduler
