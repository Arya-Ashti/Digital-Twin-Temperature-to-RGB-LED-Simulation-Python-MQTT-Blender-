import paho.mqtt.client as mqtt

# MQTT Configuration
host = "localhost"  # Running locally
port = 1883
topic_pub = "led/rgb"   # Publish RGB values to this topic
topic_sub = "sensor/temperature"  # Listen to this topic (Subscribe to sensor readings)
client_id = "LED_RGB_Controller"

# Function to map temperature to RGB values
def temperature_to_RGB(temperature):
    if temperature == 17:
        return (255, 0, 0, "red")      # Red
    elif temperature == 18:
        return (255, 165, 0, "orange")    # Orange
    elif temperature == 19:
        return (255, 255, 0, "yellow")    # Yellow
    elif temperature == 20:
        return (0, 255, 0, "green")      # Green
    elif temperature == 21:
        return (0, 0, 255, "blue")      # Blue
    elif temperature == 22:
        return (75, 0, 130, "indigo")     # Indigo
    elif temperature == 23:
        return (148, 0, 211, "violet")    # Violet
    else:
        return (0, 0, 0, "off")        # Off / Black for out of range

# MQTT Callbacks
def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode())   # msg comes as bytes, decode to string then convert to float
    temperature_rounded = round(temperature)    # Round to nearest integer for mapping
    if 17 <= temperature_rounded <= 23:
        r, g, b, color_name = temperature_to_RGB(temperature_rounded) # Get RGB values and color name
        client.publish(topic_pub, f"{r},{g},{b},{color_name}") # Publish RGB values
        print(f"Temp {temperature_rounded} → RGB {r},{g},{b} → Color: {color_name}")    # Log the mapping
    else:
        print(f"Temperature: {temperature_rounded}°C is out of range for RGB mapping.") # Log out of range

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        client.subscribe(topic_sub) # Subscribe to sensor topic to listen for temperature readings
    else:
        print("Connection failed")

# MQTT Client Setup
client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT Broker
client.connect(host, port)
client.loop_forever() 
