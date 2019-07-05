'''
Created on 26 jun. 2019

@author: jrangel
'''

from subprocess import call

import read_mango_humidity
#import read_rasp_temp

call([‘espeak “Staring main.py that uploads Humidity and Rasp Temp” 2>/dev/null’], shell=True)       #sudo apt-get install espeak

# Run until you get a ctrl^c
try:
    while True:
        read_mango_humidity .   getMangoHumidity()
        #read_rasp_temp      .   getRaspTemp()
except KeyboardInterrupt:
    pass
