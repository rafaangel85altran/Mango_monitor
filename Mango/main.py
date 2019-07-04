'''
Created on 26 jun. 2019

@author: jrangel
'''

import sys
import read_mango_humidity
import read_rasp_temp
sys.path.insert(0, 'C:\Users\jrangel\git\Mango_monitor\Mango')

# Run until you get a ctrl^c
try:
    while True:
        read_mango_humidity .   getMangoHumidity()
        read_rasp_temp      .   getRaspTemp()
except:
    print("Error during execution, finishing")
