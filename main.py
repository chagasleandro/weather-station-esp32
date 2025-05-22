from lib import wifi, dht_sensor, mqtt_client
import time

wifi.connect()
mqtt = mqtt_client.connect()

while True:
    temp, hum = dht_sensor.read()
    if temp is not None and hum is not None:
        mqtt.publish("estacao/temperatura", str(temp))
        mqtt.publish("estacao/umidade", str(hum))
    time.sleep(60)  # aguarda 1 minuto
