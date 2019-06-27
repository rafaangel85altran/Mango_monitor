'''
Created on 26 jun. 2019

@author: jrangel
'''

import time
import paho.mqtt.client as mqtt
import json
from read import getSerialData

THINGSBOARD_HOST = 'demo.thingsboard.io'
#THINGSBOARD_HOST = '192.168.1.213'
port = 1883
username = "Ms8CnTBBIhUvDdEsxs19"           # Raspberry pi Roja
password=""
topic="v1/devices/me/telemetry"
INTERVAL=2                                  # Data capture and upload interval in seconds.
sensor_data = {'humidity': 0}
next_reading = time.time() 
client = mqtt.Client()
client.username_pw_set(username, password)  # Set access token

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, port, 60)
client.loop_start()

humidity = 1

try:
    while True:
        #humidity = int(getSerialData())
        '''
        try:
            humidity = getSerialData()
            print(u"Humidity: {:g}%".format(humidity))
            sensor_data['humidity'] = humidity
            client.publish(topic, json.dumps(sensor_data), 1)   # Sending humidity and temperature data to ThingsBoard
        except:
            humidity = None
            print "Humidity could not be stored"
        '''
        humidity += 1
        if humidity > 10:
            humidity = 0
        
        print(u"Humidity: {:g}%".format(humidity))
        sensor_data['humidity'] = humidity
        client.publish(topic, json.dumps(sensor_data), 1)   # Sending humidity and temperature data to ThingsBoard
            
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()