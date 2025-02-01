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
# use motor.py in same folder (TB6612FNG)
# H-Bridge Motor Controler Directly in code..


#~~~~~~~~~ Imports ~~~~~~~~~~~~~~~
import sys
import time

import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.UART as UART
#from motor import *
import serial

print(sys.version)

#~~~~~~~~~ Motor Deffinitions ~~~~~~
    
# Motor A = Left
# Motor B = Right
# Pin Number, NOT Linux GPIO Number (Change for PocketBeagle)

ain1 = 13
ain2 = 15
bin1 = 16
bin2 = 18

#my_pwm0a = "P1_36"   # PWM0-A
#my_pwm0b = "P1_33"   # PWM0-B

#~~~~~~~~~ UART Settings ~~~~~~~~~~

UART.setup("PB-UART1")		# pins 2_05 and 2_07

ser = serial.Serial(port = "/dev/ttyO4", baudrate=9600)		# tty04 for serial1? need to check that.. doesnt work with tty01 for serial1
ser.close()
ser.open()
if ser.isOpen():
    print ("Serial1 is open!")
    #ser.write("Hello World!")

#~~~~~~~~~~~ Setup ~~~~~~~~~~~~~
#print("Python Version: " + sys.version)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ain1,GPIO.OUT)
GPIO.setup(ain2,GPIO.OUT)
GPIO.setup(bin1,GPIO.OUT)
GPIO.setup(bin2,GPIO.OUT)

#~~~~~~~~~~ Functions ~~~~~~~~~~

def forward():
    GPIO.output(ain1,True)        
    GPIO.output(ain2,False)
    GPIO.output(bin1,True)
    GPIO.output(bin2,False)
    sleep(0.1)
        

def back():
    GPIO.output(ain1,False)        
    GPIO.output(ain2,True)
    GPIO.output(bin1,False)
    GPIO.output(bin2,True)
    sleep(0.1)
        

def right():
    GPIO.output(ain1,True)        
    GPIO.output(ain2,False)
    GPIO.output(bin1,False)
    GPIO.output(bin2,True)
    sleep(0.1)
        

def left():
    GPIO.output(ain1,False)        
    GPIO.output(ain2,True)
    GPIO.output(bin1,True)
    GPIO.output(bin2,False)
    sleep(0.1)
        
def stop():
    GPIO.output(ain1,False)        
    GPIO.output(ain2,False)
    GPIO.output(bin1,False)
    GPIO.output(bin2,False)
    #sleep(2)


#~~~~~~~~~~~ While Loop ~~~~~~~~~~~~~~

while True:
       data = ser.readline(1)		# read from bluetooth (size of bytes rt read)

       #if data:					# if data is present from bluetooth
           #print(data.decode("utf-8"))		# print data to console.remove \r\n line endings

       if data.decode("utf-8") == "B":
           print("Brake")
           stop()

       elif data.decode("utf-8") == "W":   
           print("forward") 
           forward()
           #r2.speak("hjk")

       elif data.decode("utf-8") == "A":  
           print("left") 
           left()

       elif data.decode("utf-8") == "S":
           print("back") 
           back()

       elif data.decode("utf-8") == "D":
           print("right")
           right()

       elif data.decode("utf-8") == "C":
           print("C-Button")

           
       else: stop()


GPIO.cleanup()
ser.close()
# EOF







ser.close()
GPIO.cleanup()
PWM.stop(my_pwm0a)
PWM.stop(my_pwm0b)
PWM.cleanup()


