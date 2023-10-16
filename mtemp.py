#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)

# get setting temperature
temp = b'\x04\x32\x37\x4D\x31\x05'
ser.write(temp)  # send command to the chiller for get temp setting
line = ser.readline()  
print(line)
line2 = line.strip().decode("utf-8")
b=line2.split()
print("measurement temp ",b[1][:-1])
c=float(b[1][:-2])
#d=c+x
print(c)
print("")
