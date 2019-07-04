'''
Created on 4 jul. 2019

@author: jrangel
'''

import time
from main import interval
from main import client

# think of measurement as a SQL table, it's not...but...
measurement = "test saw"
# location will be used as a grouping tag later
location = "ZGZ Boggiero"
room = "Terraza"
place = "Maceta Mango"

data_test = 0


def getMangoHumidity():
    # Data to store
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
              "room"    : room,
              "place"   : place
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