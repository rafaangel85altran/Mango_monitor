'''
Created on 26 jun. 2019

@author: jrangel
'''

import time
import sys
import datetime
from influxdb import InfluxDBClient

# Configure InfluxDB connection variables
host = "192.168.1.213"                          # My Ubuntu NUC
port = 8086                                     #default port
user = "admin"                                  # the user/password created for the pi, with write access
password = "emperador" 
dbname = "telegraf"                             #the database we created earlier
interval = 5                                    #Sample period in seconds

# Create the InfluxDB client object
client = InfluxDBClient(host, port, user, password, dbname)

# Enter the sensor details
sensor = 0
sensor_gpio = 0

# think of measurement as a SQL table, it's not...but...
measurement = "test saw"
# location will be used as a grouping tag later
location = "ZGZ Boggiero"

data_test = 0

# Run until you get a ctrl^c
try:
    while True:
        # Read the sensor using the configured driver and gpio
        data_test = 2 + data_test 
        iso = time.ctime()
        # Print for debugging, uncomment the below line
        # print("[%s] Temp: %s, Humidity: %s" % (iso, temperature, humidity)) 
        # Create the JSON data structure
        data = [
        {
          "measurement": measurement,
              "tags": {
                  "location": location,
              },
              "time": iso,
              "fields": {
                  "temperature" : data_test
              }
          }
        ]
        # Send the JSON data to InfluxDB
        client.write_points(data)
        # Wait until it's time to query again...
        time.sleep(interval)
        if (data_test > 25):
            data_test = 0
        print("Sending", data_test,"...")    
            
except KeyboardInterrupt:
    pass
