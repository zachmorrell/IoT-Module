import wlan_connection as wlan
import mqtt_connection as mqtt
import temp_hum_sensors as sensors
import utime as time
def main():
    # Connect to Wi-Fi
    wlan.connect()
    time.sleep(1)
    
    # Connect to mqtt broker
    mqtt.activate_mqtt()
    time.sleep(1)
    
    # Run board scripts
    while True:
        # Publish's data to broker.
        mqtt.publish_topic(sensors.print_stats())
        # Checks sub for new instructions.
        mqtt.check_sub()
        # Sleep for 5 seconds.
        time.sleep(5)
main()