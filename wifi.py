import network
import time

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    try:
        wlan.connect(ssid, password)
        start = time.time()
        while not wlan.isconnected() and time.time() - start < 20:
            pass
        if wlan.isconnected():
            # Verbinding is gemaakt
            print('Verbonden met WiFi-netwerk')
            print('IP-adres:', wlan.ifconfig()[0])
        else:
            # Fout bij het verbinden na 20 seconden
            print('Kan geen verbinding maken met het WiFi-netwerk. Controleer de SSID en het wachtwoord')

    except:
        # Fout bij het verbinden
        print('Kan geen verbinding maken met het WiFi-netwerk. Controleer de SSID en het wachtwoord')

def check_wifi_connection():
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        print("ESP32 is verbonden met WiFi")
    else:
        print("ESP32 is niet verbonden met WiFi")
        

