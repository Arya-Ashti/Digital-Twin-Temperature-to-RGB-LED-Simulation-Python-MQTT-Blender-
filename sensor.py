import paho.mqtt.client as mqtt
import time
import random

# MQTT Configuration
host = "localhost"  # Running locally
port = 1883
topic = "sensor/temperature"    # Sensor will publish to this topic
client_id = "temperature_RGB"

# Sensor Simulation Configuration
initial_temperature = 20.0  
min_temp, max_temp = 17.0, 23.0 # 7 degree temperature range to easily visualise changes, can be adjusted as needed
update_interval = 1 # How often to publish temperature readings (in seconds)

# MQTT Callbacks 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connection failed")
    print("Connected with result code " + str(rc))


def on_disconnect(client, userdata, rc):
    print("Disconnected")

# MQTT Client Setup
client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Connect to MQTT Broker
client.connect(host, port)
client.loop_start()

# Simulate Temperature Sensor
current_temperature = initial_temperature

# Publish simulated temperature readings
while True:
    current_temperature += random.uniform(-1, 1) # small random walk
    current_temperature = max(min(current_temperature, max_temp), min_temp)     # clamp to min/max
    client.publish(topic, current_temperature)  # Publish temperature reading
    print(f"Publishing temperature: {current_temperature:.2f}")  # Log published temperature
    time.sleep(update_interval) # Wait before next reading