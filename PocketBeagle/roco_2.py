#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# last edit 08/03/2023
#
# Roco Robot Companion
# PocketBeagle - Body
#
# PIP Packages:
#
# pip3 install beepy
# pip3 install adafruit-circuitpython-pca9685
# pip3 install pyserial
# pip3 install pyaudio
# pip3 install Adafruit_BBIO
# pip3 install HC-05-ConfigTool
#
#
#
# Linux Dependant Packages:
#
# sudo apt-get install build-essential python3-dev python3-pip portaudio19-dev python3-all-dev -y
#
#
# for Motor Driver use motor.py in same folder:
# Motor(IN1,IN2,PWM,STANDBY,(Reverse polarity?))
# M1 = Motor(13,19,P1_33,6,False)    # CHECK/CHANGE NUMBERS FOR POCKETBEAGLE
# M2 = Motor(13,19,P1_36,6,False)    # CHECK/CHANGE NUMBERS FOR POCKETBEAGLE
#
# M1.drive(100) #Forward 100% dutycycle
# sleep(1)
# M1.drive(-100) #Backwards 100% dutycycle
# sleep(1)
# M1.brake() #Short brake
# sleep(0.1)
# M1.standby(True) #Enable standby
# M1.standby(False) #Disable standby

# Imports:
import sys
import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.UART as UART
from Adafruit_BBIO.SPI import SPI
import serial
import pyaudio
from ttastromech import TTAstromech
import os
import psutil
import datetime
import time as ti
from motor import *
from Adafruit_I2C import Adafruit_I2C




# ~~~~~~~~~~~~~~ Name Settings ~~~~~~~~~~~~

user = "Daniel"
SN = "Roco"

# ~~~~~~~~~~~~~ Main Setup ~~~~~~~~~~~~

r2 = TTAstromech()
r2.speak("eo")		# 
ti.sleep(2)
r2.speak("eeo")		# 
ti.sleep(2)
r2.speak("eeeo")
ti.sleep(2)
r2.speak("ooo")

mypin = "USR3"  # LED USR3
GPIO.setup(mypin, GPIO.OUT)

i2c = Adafruit_I2C(0x77)    # default is I2C-1

spi0 = SPI(1, 0)
spi1 = SPI(1, 1)

UART.setup("PB-UART2")  # RX,TX pins 1_08 and 1_10 /dev/ttyO2  (SPI0 Pins CLK, MISO)
UART.setup("PB-UART1")  # RX,TX pins 2_05 and 2_07 /dev/ttyO4

# ~~~~~~~~ HC-05 Bluetooth Port ~~~~~~~~

serblu = serial.Serial(port="/dev/ttyO4",
                    baudrate=9600)  # tty04 for serial1? need to check that.. doesnt work with tty01 for serial1
serblu.close()
serblu.open()

# ~~~~~~~~ Nano pi Serial Communications Port ~~~~~~~

serpi = serial.Serial(port="/dev/ttyO2",
                    baudrate=9600)  
serpi.close()
serpi.open()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Command Definitions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def greet():
    hour = datetime.datetime.now().hour
    if (hour >= 0) and (hour < 12):
        r2.speak("abg")
    elif (hour >= 12) and (hour < 18):
        r2.speak("tfs")
    elif (hour >= 18) and (hour < 24):
        r2.speak("qaef")

def reboot():
    os.system("python3 ~/roco.py")
    exit()

def shutdown():
    os.system('systemctl poweroff')

#
# More Commands Here ^^^^^
#

# ~~~~~~~~~~~~~ Main Code ~~~~ Run Once ~~~~~~~~~~~~~~~~~
# print python version
print("~~~~~~~~~~~~~~~~~~~~~")
print("Python Version: " + sys.version)

print("~~~~~~~~~~~~~~~~~~~~~")
print("Power-On Time: " + datetime.datetime.now().strftime("%H:%M"))

if serblu.isOpen():
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("Serial-Blu is open!")
    print("~~~~~~~~~~~~~~~~~~~~~")
if serpi.isOpen():
    print("Serial-Pi is open!")
    print("~~~~~~~~~~~~~~~~~~~~~")

greet()

# ~~~~~~~~~~~~~ Main Code ~~~~ Loop the following ~~~~~~~


try:
    while True:

        # ~~~~~~~~~~~~~ Main Code ~~~~ Listen for Bluetooth Controller ~~~~~~~

        
        dataserblu= serblu.readline(1)  # read from bluetooth (size of bytes to read)
        dataserpi= serpi.readline(1)  # read from USB (size of bytes to read)

        # if dataserblu:    # if data is present from bluetooth
            #print(dataserblu.decode("utf-8"))    # print data to console.remove \r\n line endings

        if dataserblu.decode("utf-8") == "W":  # if data is present from bluetooth.remove \r\n and compaire the remaining
            print("forward")  # print data to console

        if dataserblu.decode("utf-8") == "S":  # if data is present from bluetooth.remove \r\n and compaire the remaining
            print("back")  # print data to console

        if dataserblu.decode("utf-8") == "A":  # if data is present from bluetooth.remove \r\n and compaire the remaining
            print("left")  # print data to console

        if dataserblu.decode("utf-8") == "D":  # if data is present from bluetooth.remove \r\n and compaire the remaining
            print("right")  # print data to console

        if dataserblu.decode("utf-8") == "C":  # if data is present from bluetooth.remove \r\n and compaire the remaining
            print("C-Button")  # print data to console

        if dataserblu.decode("utf-8") == "Z":  # if data is present from bluetooth.remove \r\n and compaire the remaining
            print("Brake")  # print data to console

#
#
#
#
#
#

except Exception as e:
    raise e
finally:
    print("cleanup")
    GPIO.output(mypin, GPIO.LOW)
    spi0.close()
    spi1.close()
    GPIO.cleanup()

# ~~~~~~~~~~~~~~ EOF ~~~~~~~~~~~~~

