'''
Created on 4 jul. 2019

@author: PC
'''
import serial

def getSerialData ():

    try: 
        ser = serial.Serial('COM4', 9600) 
        serial_line = ser.readline()
        #print(serial_line)
        ser.close()
    except: 
        #print ("Port coudnt be opened")
        serial_line = ""
    return serial_line