'''
Created on 26 jun. 2019

@author: jrangel
'''

import read_mango_humidity
import read_rasp_temp

# Run until you get a ctrl^c
try:
    while True:
        read_mango_humidity .   getMangoHumidity()
        read_rasp_temp      .   getRaspTemp()
except:
    print("Error during execution, finishing")
