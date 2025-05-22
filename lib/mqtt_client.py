from umqtt.simple import MQTTClient

MQTT_BROKER = "IP_DO_BROKER"
CLIENT_ID = "esp32-weather"
TOPIC_TEMP = b"estacao/temperatura"
TOPIC_UMID = b"estacao/umidade"

def connect():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER)
    client.connect()
    print("Conectado ao broker MQTT!")
    return client
