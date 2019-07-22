'''
Created on 4 jul. 2019

@author: jrangel
'''

import time
from influxdb import InfluxDBClient


from read_serial import getSerialData

# Configure InfluxDB connection variables
host = "localhost"                          	# Raspberri pi Roja Ip en ZGZ
port = 8086                                     #default port for InfluxDB
user = "admin"                                  # the user/password created for influxDB
password = "emperador" 
dbname = "telegraf"                             #the database we created earlier
interval = 60                                    #Sample period in seconds

# think of measurement as a SQL table, it's not...but...
measurement = "Humedad maceta"
# location will be used as a grouping tag later
location = "ZGZ Boggiero"
room = "Despacho"
place = "vaso agua"

# Create the InfluxDB client object
clientMango = InfluxDBClient(host, port, user, password, dbname)

def getMangoHumidity():
    # Data to store
    data_test = float(getSerialData())
    #data_test = 3
     
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
              "pH" : data_test
              }
      }
    ]

    # Send the JSON data to InfluxDB
    clientMango.write_points(data)
    # Wait until it's time to query again...
    time.sleep(interval)
    print(iso,"pH" , data_test, "%")    