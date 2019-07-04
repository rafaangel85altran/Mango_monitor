'''
Created on 4 jul. 2019

@author: jrangel
'''
import os
import time
from main import interval
from main import client

# think of measurement as a SQL table, it's not...but...
measurement = "test saw"
# location will be used as a grouping tag later
location = "ZGZ Boggiero"
room = "Terraza"
place = "Raspberry Pi Roja"

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp)

def getRaspTemp():
    iso = time.ctime()              #Store time    
    data = [
    {
      "measurement": measurement,
          "tags": {
              "location": location,
              "room"    : room,
              "place"   : place
          },
          "time": iso,
          "fields": {
              "temperature" : measure_temp()
          }
      }
    ]
    # Send the JSON data to InfluxDB
    client.write_points(data)
    time.sleep(interval)
    print("Sending", measure_temp(),"...") 