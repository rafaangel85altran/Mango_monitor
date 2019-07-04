'''
Created on 4 jul. 2019

@author: jrangel
'''
import os
import re
import time
from influxdb import InfluxDBClient

# Configure InfluxDB connection variables
host = "localhost"                          # Raspberri pi Roja Ip en ZGZ
port = 8086                                     #default port for InfluxDB
user = "admin"                                  # the user/password created for influxDB
password = "emperador" 
dbname = "telegraf"                             #the database we created earlier
interval = 5                                    #Sample period in seconds

# think of measurement as a SQL table, it's not...but...
measurement = "temperatura raspberry"
# location will be used as a grouping tag later
location = "ZGZ Boggiero"
room = "Terraza"
place = "Raspberry Pi Roja"

clientRasp = InfluxDBClient(host, port, user, password, dbname)

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        rasp_temp = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", temp)
                
        return (rasp_temp)

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
          "fields": {
              "temperature" : measure_temp()
          }
      }
    ]
    # Send the JSON data to InfluxDB
    clientRasp.write_points(data)
    time.sleep(interval)
    print(iso,"Temperatura" , measure_temp(), "grados")     