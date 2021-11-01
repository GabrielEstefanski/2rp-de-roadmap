from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from custom_operators.tworp_spark_submit_operator import TwoRPSparkSubmitOperator
from datetime import datetime

usuario = "2rp-gabrielb"
default_args={
    "owner":"2rp-gabrielb",
    "start_date": datetime(2021,10,20),
    "depend_on_past": False,
    "run_as_user": usuario,
    "proxy_user": usuario
}

with DAG(dag_id='de_gabriel_braga_dev', schedule_interval=None, default_args = default_args, catchup=False) as dag:

        t_dummy = DummyOperator(
                task_id='dummy_task',
        )

        t_kinit = BashOperator(
                task_id='kinit_task',
                bash_command=f'kinit -kt /home/{usuario}/{usuario}.keytab {usuario}'
        )

        t_shell = BashOperator(
                task_id='shell_task',
                bash_command=f'sh /home/{usuario}/shell-script/executar.sh /home/{usuario}/teste-shell mensagem_shell_task'
        )

        t_spark = TwoRPSparkSubmitOperator(
                task_id='spark_task',
                name='spark_task',
                conn_id='spark_conn',
                application=f'/home/{usuario}/pokemons_oldschool.py',
                keytab=f'/home/{usuario}/{usuario}.keytab',
                principal=usuario,
                proxy_user=None,
                verbose=True
        )

        t_dummy >> t_kinit >> t_shell >> t_spark

