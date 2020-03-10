'''
Created on 26 jun. 2019

@author: jrangel
'''

import time
import read_pool_ph
import read_rasp_temp

#Sample period in seconds
interval = 60                                    

#Wait at least 60seconds so the rasp can connect to the Wifi

time.sleep(interval)

# Run until you get a ctrl^c
try:
    while True:
        read_pool_ph.getPoolPH()
        read_rasp_temp.getRaspTemp()
        time.speed(interval)
except KeyboardInterrupt:
    pass
