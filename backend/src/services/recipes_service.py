from src.config.mqtt import mqtt_client

class RecipeService:
    def start(self, flavor: str, liters: int):
        # Aqui no futuro você salvaria no banco de dados (MySQL)

        grams = liters * 15 # Formula teste

        topic = f"factory/recipes/{flavor}_doser/doser/cmd"
        payload = f"START:{grams}"
        mqtt_client.publish(topic, payload)

        # Retorna os dados para quem chamou (o Controller)
        return True