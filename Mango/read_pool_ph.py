'''
Created on 4 jul. 2019

@author: jrangel
'''

import time
from influxdb import InfluxDBClient
from read_serial import getSerialData

# Configure InfluxDB connection variables
host = "localhost"                              # Raspberri pi Roja Ip en ZGZ
port = 8086                                     # default port for InfluxDB
user = "admin"                                  # the user/password created for influxDB
password = "emperador" 
dbname = "telegraf"                             #the database we created earlier

# think of measurement as a SQL table, it's not...but...
measurement = "pH Piscina"
# location will be used as a grouping tag later
location = "ZGZ Boggiero"
room = "Terraza"
place = "Terraza"

# Create the InfluxDB client object
clientMango = InfluxDBClient(host, port, user, password, dbname)

def getPoolPH():
    # Data to store
    data_received = float(getSerialData())
     
    iso = time.ctime()
    data = [
    {
      "measurement": measurement,
          "tags": {
              "location": location,
              "room"    : room,
              "place"   : place 
          },
          "fields": { 
              "pH" : data_received
              }
      }
    ]

    # Send the JSON data to InfluxDB
    clientMango.write_points(data)
    # Wait until it's time to query again...
    print(iso,"pH" , data_received, "pH")    