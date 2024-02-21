import utime as time
from umqtt.simple import MQTTClient

mqtt_server = 'test.mosquitto.org'
client_id = 'Zach'
    
def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.set_callback(sub_cb)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()
    
def activate_mqtt():
    try:
        global client
        print('attempting to connect to mqtt broker')
        client = mqtt_connect()
    except OSError as e:
        reconnect()
        time.sleep(3)

# Function to check the topic for new posts.
def check_sub():
    client.subscribe(b'/cit220/test')

# Function to decode message from subscribed topic.
def sub_cb(topic, msg):
    msg = msg.decode('utf-8')
    print(msg)

# Function to publish to mqtt server.
def publish_topic(topic_msg):
    topic_pub = b'/cit220/test'
    client.publish(topic_pub, topic_msg)