# src/config/mqtt.py
import paho.mqtt.client as mqtt
from src.handlers.status_handler import processar_mensagem_status

BROKER_IP = "mosquitto"
mqtt_client = mqtt.Client()

def ao_conectar(client, userdata, flags, rc):
    print("✅ [MQTT] Conectado ao Broker com sucesso!")
    client.subscribe("factory/#")
    print("📥 [MQTT] Inscrito no tópico factory/#")

def ao_receber_mensagem(client, userdata, msg):
    payload = msg.payload.decode()
    
    processar_mensagem_status(msg.topic, payload)

# Atribui os callbacks
mqtt_client.on_connect = ao_conectar
mqtt_client.on_message = ao_receber_mensagem

def iniciar_mqtt():
    mqtt_client.connect(BROKER_IP, 1883, 60)
    mqtt_client.loop_start()