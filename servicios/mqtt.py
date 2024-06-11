import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from colorama import Fore, Back, Style, init



print("mqtt client")

init() # init colorama (Despues agregare color al print del terminal)
# Carga las variables de entorno desde el archivo .env
load_dotenv()
# Accede a las variables de entorno cargadas
MQTT_URL = os.getenv("MQTT_URL")
MQTT_PORT =1883
TOPICS_LIST = ["/REQ"]




USERS =[
    "1234",
    "593189658514",
]


def process_req(client,product_id,user_id):
    topic= None
    if user_id in USERS:
        print("Usuario valido")
        topic="/RES/OK"
    else:
        print("Usuario invalido")
        topic="/RES/FAIL"
    client.publish(f"{product_id}{topic}",f"{product_id}",qos=2,retain=False)

def on_connect(client, userdata, flags, rc):
    print("Conectado a Broker mqtt")

    # The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
     global last_command
     data = msg.payload.decode('utf-8')
     topic = msg.topic
     product_id,user_id = data.split(",") 
     print(f"Product ID: {product_id}\nUserID: {user_id}")
     process_req(client,product_id,user_id)






def get_client():
        # The callback for when the client receives a CONNACK response from the server.


    

    
    client = mqtt.Client(clean_session = True)
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect(MQTT_URL,MQTT_PORT,60)
        for e in TOPICS_LIST:
            print(f"sub a {e}")
            client.subscribe(e)
    except Exception as e:
        print(f"Error:{e}")
    return client
    

