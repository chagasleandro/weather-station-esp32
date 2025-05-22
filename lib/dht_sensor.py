import dht
from machine import Pin

sensor = dht.DHT22(Pin(4))  # GPIO4

def read():
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temp:", temp, "Hum:", hum)
        return temp, hum
    except Exception as e:
        print("Erro ao ler o sensor:", e)
        return None, None
