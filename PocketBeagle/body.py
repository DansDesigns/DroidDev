#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#	Roco controller - body control
#
#
#
#
#
# pip3 install pyserial
#
#
#
# use motor.py in same folder

import sys
import time

import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.UART as UART
from motor import *
import serial

print(sys.version)

my_pwm0a = "P1_36"   # PWM0-A
my_pwm0b = "P1_33"   # PWM0-B

PWM.start(my_pwm0a)
PWM.start(my_pwm0b)

#Motor(AIN1,AIN2,PWM,STANDBY,(Reverse polarity?))
M1 = Motor(13,19,my_pwm0a,6,False)		# Left  Motor = A
M2 = Motor(13,19,my_pwm0b,6,False)		# Right Motor = B


UART.setup("PB-UART1")		# pins 2_05 and 2_07

ser = serial.Serial(port = "/dev/ttyO4", baudrate=9600)		# tty04 for serial1? need to check that.. doesnt work with tty01 for serial1
ser.close()
ser.open()
if ser.isOpen():
    print ("Serial1 is open!")
    #ser.write("Hello World!")


while True:
       M1.standby(True) #Enable standby
       M2.standby(True) #Enable standby
       data = ser.readline(1)		# read from bluetooth (size of bytes rt read)

       #if data:					# if data is present from bluetooth
           #print(data.decode("utf-8"))		# print data to console.remove \r\n line endings

       if data.decode("utf-8") == "W":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           M1.standby(False) #Disable standby
           M2.standby(False) #Disable standby
           print("forward")				# print data to console
           M1.drive(100)				# drive forward 100% speed
           M2.drive(100)
           M1.brake()
           M2.brake()
           delay(0.3)


       if data.decode("utf-8") == "S":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           M1.standby(False) #Disable standby
           M2.standby(False) #Disable standby

           print("back")				# print data to console
           M1.drive(-100)				# drive forward 100% speed
           M2.drive(-100)
           M1.brake()
           M2.brake()
           delay(0.3)


       if data.decode("utf-8") == "A":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           M1.standby(False) #Disable standby
           M2.standby(False) #Disable standby

           print("left")				# print data to console
           M1.drive(100)				# drive forward 100% speed
           M2.drive(100)
           M1.brake()
           M2.brake()
           delay(0.3)


       if data.decode("utf-8") == "D":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           M1.standby(False) #Disable standby
           M2.standby(False) #Disable standby

           print("right")				# print data to console
           M1.drive(100)				# drive forward 100% speed
           M2.drive(100)
           M1.brake()
           M2.brake()
           delay(0.3)


       if data.decode("utf-8") == "C":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           print("C-Button")				# print data to console

       if data.decode("utf-8") == "Z":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           M1.standby(False) #Disable standby
           M2.standby(False) #Disable standby

           print("Brake")				# print data to console
           M1.brake()
           M2.brake()






ser.close()
GPIO.cleanup()
PWM.stop(my_pwm0a)
PWM.stop(my_pwm0b)
PWM.cleanup()


