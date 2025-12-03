# Digital-Twin-Temperature-to-RGB-LED-Simulation-Python-MQTT-Blender-
This project simulates a temperature sensor and visualises the data using a digital twin built in Blender. The system uses MQTT to communicate temperature readings and RGB LED values in real time.

# Structural Overview
<img width="679" height="72" alt="structural overview" src="https://github.com/user-attachments/assets/75527667-3cac-4cb4-9867-e93c4ff24076" />
- sensor.py simulates a live temperature using a random walk and publishes values to sensor/temperature.

- led.py subscribes to the temperature, converts it into corresponding RGB values, and publishes them to led/rgb.

- Blender subscribes to led/rgb and updates the colour of a 3D object in real time.

This creates a complete IT/OT system with a digital twin visualisation.

# Features
1) Real-time sensor simulation and visualiser
   - Ranndom temperature Walk
   - configurable intervals and bounds

2) MQTT-based communication (Mosquitto + Paho-MQTT)
   - sensor/temperature → raw temperature
   - led/rgb → RGB colour mapping

3) Temperature to RGB Mapping logic:

| Temperature (°C) | Colour | RGB         |
| ---------------- | ------ | ----------- |
| 17               | Red    | (255,0,0)   |
| 18               | Orange | (255,165,0) |
| 19               | Yellow | (255,255,0) |
| 20               | Green  | (0,255,0)   |
| 21               | Blue   | (0,0,255)   |
| 22               | Indigo | (75,0,130)  |
| 23               | Violet | (148,0,211) |

