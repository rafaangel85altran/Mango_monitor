'''
Created on 4 jul. 2019

@author: jrangel
'''

import time
#from main import interval
from influxdb import InfluxDBClient

# Configure InfluxDB connection variables
host = "192.168.1.213"                          # Raspberri pi Roja Ip en ZGZ
port = 8086                                     #default port for InfluxDB
user = "admin"                                  # the user/password created for influxDB
password = "emperador" 
dbname = "telegraf"                             #the database we created earlier
interval = 5                                    #Sample period in seconds

# think of measurement as a SQL table, it's not...but...
measurement = "test saw"
# location will be used as a grouping tag later
location = "ZGZ Boggiero"
room = "Terraza"
place = "Maceta Mango"
data_test = 0

# Create the InfluxDB client object
clientMango = InfluxDBClient(host, port, user, password, dbname)

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
    clientMango.write_points(data)
    # Wait until it's time to query again...
    time.sleep(interval)
    print("Sending", data_test,"...")    