'''
Created on 26 jun. 2019

@author: jrangel
'''

import time
import paho.mqtt.client as mqtt
import json
from read import getSerialData

THINGSBOARD_HOST = 'demo.thingsboard.io'
port = 1883
username = "Ms8CnTBBIhUvDdEsxs19"
password=""
topic="v1/devices/me/telemetry"


# Data capture and upload interval in seconds.
INTERVAL=2

sensor_data = {'humidity': 0}

next_reading = time.time() 

client = mqtt.Client()

# Set access token
client.username_pw_set(username, password)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, port, 60)

client.loop_start()

try:
    while True:
        humidity = int(getSerialData())
        #humidity = 1;
        print(u"Humidity: {:g}%".format(humidity))
        sensor_data['humidity'] = humidity

        # Sending humidity and temperature data to ThingsBoard
        client.publish(topic, json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()