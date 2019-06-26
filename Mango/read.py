'''
Created on 26 jun. 2019

@author: jrangel
'''
import serial

def getSerialData ():

    try: 
        ser = serial.Serial('COM1', 9600) 
        serial_line = ser.readline()
        print(serial_line)
        ser.close()
    except: 
        print "Port coudnt be opened"
        serial_line = ""
    return serial_line

