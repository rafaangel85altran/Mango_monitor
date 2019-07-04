'''
Created on 26 jun. 2019

@author: jrangel
'''

import sys
import read_mango_humidity
sys.path.insert(0, 'C:\Users\jrangel\git\Mango_monitor\Mango')

from influxdb import InfluxDBClient

# Configure InfluxDB connection variables
host = "192.168.1.213"                          # Raspberri pi Roja Ip en ZGZ
port = 8086                                     #default port for InfluxDB
user = "admin"                                  # the user/password created for influxDB
password = "emperador" 
dbname = "telegraf"                             #the database we created earlier
interval = 5                                    #Sample period in seconds

# Create the InfluxDB client object
client = InfluxDBClient(host, port, user, password, dbname)

# Run until you get a ctrl^c
try:
    while True:
        read_mango_humidity.getMangoHumidity()
except KeyboardInterrupt:
    pass
except:
    print("Error during execution, finishing")
