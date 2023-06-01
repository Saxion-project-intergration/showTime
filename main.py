import wifi
import _thread
import getTime
import printData
# SSID en wachtwoord van het WiFi-netwerk
wifi_ssid = 'Michiel de router'
wifi_password = 'Roeswifi28'

# Verbinding maken met WiFi-netwerk
wifi.connect_to_wifi(wifi_ssid, wifi_password)

# Example usage
time_str = getTime.get_local_time_string()
print("Local Time: ", time_str)

while true:
    printData.printText("backend = frontend)
    time.sleep(10)