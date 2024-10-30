# Importing the libraries
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
# from utils.utils import fetch_data,format_data
from kafka import KafkaProducer
import time
from uuid import uuid4

import requests
def fetch_data():
    import requests
    
    # Getting back the response from the request
    res = requests.get("https://randomuser.me/api/")
    res = res.json()['results'][0]
    
    return res
    
# Now, the respone has too many info, we need to extract the ones whe truly need
def format_data(res):
    data = {}
    data['id'] = str(uuid4())  # Generate a new UUID for each record
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['address'] = str(res['location']['street']['name'] + ' ,' + res['location']['city'] + ' ,' + res['location']['state'] + ' ,' + res['location']['country'])
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['phone'] = res['phone']
    data['profile_pic'] = res['picture']['medium']
    data['nationality'] = res['nat']
    
    return data

# Setting the default_args 
default_args = {
    'owner':"ouhami",
    'start_date':datetime(2024,10,28)
}

# Creating our task

def stream_data():
    
    # Import json and requests to make HTTP requests and parse data into JSON
    import json
    import logging
    
    
    # Now, we will need to push the new data into Kafka
    # Initializing the producer
    producer = KafkaProducer(bootstrap_servers=['broker:29092'],max_block_ms=5000)
    curr_time = time.time()
    
    while True:
        if(time.time() > curr_time + 60):
            break
        try :
            res = fetch_data()
            res = format_data(res)
            
            print(json.dumps(res))
            
            # Sending the data into Kafka
            producer.send("users_created",json.dumps(res).encode("utf-8"))
        
        except Exception as e:
            logging.error("An error has occured : " + e)
            continue
    print("Sent data to Kafka")
    
    


# # Creating our DAG
with DAG(dag_id='user_fetch_automation',default_args=default_args,schedule_interval="@daily",catchup=False):
    
    # Creating our streaming_task
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )
