import network
import time

SSID = "SEU_WIFI"
PASSWORD = "SUA_SENHA"

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando ao Wi-Fi...")
        wlan.connect(SSID, PASSWORD)
        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1
    if wlan.isconnected():
        print("Conectado! IP:", wlan.ifconfig()[0])
    else:
        print("Falha ao conectar ao Wi-Fi.")
