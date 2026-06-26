import json
from src.config.mqtt import mqtt_client

class RecipeService:
    def start(self, sabor: str, litragem: int):
        # Aqui no futuro você salvaria no banco de dados (MySQL)

        grams = litragem * 15 # Formula teste

        # Publica no MQTT
        topic = f"factory/tanks/tank1/powder/command/target_grams"
        mqtt_client.publish(topic, grams)

        topic = f"factory/tanks/tank1/powder/command/run"
        mqtt_client.publish(topic, 1) # Inicia o trabalho

        # Retorna os dados para quem chamou (o Controller)
        return True