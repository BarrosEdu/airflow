from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Default args para definir parâmetros padrão para as tarefas
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definição da DAG
dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='Uma DAG simples para teste',
    schedule_interval=timedelta(days=1),  # Executa diariamente
    start_date=datetime(2024, 1, 1),  # Data de início
    catchup=False,  # Não executar tarefas anteriores ao start_date
)

# Função Python para a tarefa
def print_hello():
    print('Hello, Airflow!')

# Definindo as tarefas
start = DummyOperator(
    task_id='start',
    dag=dag,
)

print_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

# Definindo a ordem das tarefas
start >> print_task >> end
