# Network Connection
import network
import utime as time
# umqtt.simple
#from umqtt.simple import MQTTClient
import mqtt_connection as mqtt
# SSID or Wi-Fi username
SSID = 'user'
PASSWORD = 'pass'

#Connect to WLan.
def connect():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(SSID,PASSWORD)
    print("Attempting to connect through Wi-Fi..")
    #Network: check if connected
    while not wifi.isconnected():
        pass    
    print('Connected to WiFi', wifi.ifconfig())
