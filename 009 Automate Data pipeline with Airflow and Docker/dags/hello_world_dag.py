from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'airflow',
    'depends_on_past' : False,
    'start_date' : datetime(2023, 1, 1),
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 1,
    'retry_delay' : timedelta(minutes=1)
}

def print_hello():
    print("Hello from Airflow! this pipeline is working. ")

with DAG(
    'hello_airflow_pipeline',
    default_args=default_args,
    description='A Simple test pipeline',
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:
    
    task1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    task2 = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
    )

    task1 >> task2