from datetime import datetime
import uuid
from airflow import DAG
from airflow.operators.python import PythonOperator 
import requests
import json
from kafka import KafkaProducer
import time
import logging


'''
This script is used to stream data to Kafka topic, 
followed by getting data from`randomuser.me` API,
formatting the data and sending it to Kafka topic.
and finally a dag is created to schedule the task.
'''

default_args = {
    'owner': 'Hamza',
    'depends_on_past': False,
    'start_date': datetime(2024, 7, 16),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

def get_data():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    response = response.json()
    response = response['results'][0]
    return response

def format_data(response):
    data = {}
    location = response['location']
    # data['id'] = uuid.uuid4()
    data['first_name'] = response['name']['first']
    data['last_name'] = response['name']['last']
    data['gender'] = response['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = response['email']
    data['username'] = response['login']['username']
    data['dob'] = response['dob']['date']
    data['registered_date'] = response['registered']['date']
    data['phone'] = response['phone']
    data['picture'] = response['picture']['medium'] 
    
    return data

def streaming_data():
    topic_name = 'users_created'
    # response = get_data()
    # response = format_data(response)
    # response = json.dumps(response, indent=3)
    # print(response)  
      
    producer = KafkaProducer(bootstrap_servers=['broker:29092'])

    while True:
        if time.time() > current_time + 60:
            break
        try:
            response = get_data()
            response = format_data(response)
            producer.send(topic_name, json.dumps(response).encode('utf-8'))
        except Exception as e:
            print("Failed to send data to Kafka", e)
            logging.info("Failed to send data to Kafka", e)
        finally:
            producer.close() 


'''
Creating a DAG 
'''

with DAG(
    dag_id='user_automation',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    streaming_task= PythonOperator(
        task_id='data_from_api',
        python_callable=streaming_data
    )


# streaming_data()
