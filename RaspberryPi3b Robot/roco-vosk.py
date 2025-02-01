#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# last edit 15/08/2023
# UPDATES:
# added TB6612FNG code
# added IR Sender & Receiver Code - NEED TO FINISH
# removed motor code and librarie due to lack of PWM on RPI 
#
# Roco Robot Companion
# RaspBerry Pi Version
#
# Only GPIO18 (Pin12) can do PWM..
# Motor control and Servo Control has to happen via
# either Arduino or I2C Servo-Control-Board
#
# No Built-in ADC or Analog Inputs, ALL Analog Sensors must go via Arduino Body
#
#

# Imports:
from vosk import Model, KaldiRecognizer
import sys
import time
import RPi.GPIO as GPIO
#
import serial
import pyaudio
import pyttsx3
import datetime
from datetime import timedelta
import time as ti
import os
import psutil
import pyjokes
import requests
import smtplib
import webbrowser as we
from email.message import EmailMessage
from time import sleep
import wikipedia
import random
import vlc
import ast
from ttastromech import TTAstromech
from chatterbot import ChatBot
import subprocess
import socket
import shutil



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~ Droid Speech Settings~~~~~~~~~~
r2 = TTAstromech()
r2.speak("er")			# loading

#r2.speak("ybe")		# greeting
#r2.speak("ooo")		# done/complete/finished
#r2.speak("eo")			# loading
#r2.speak("eeo")		# loading more
#r2.speak("oops")		# oops
#r2.speak("hjk")		# buzz exclimation
#r2.speak("qwerty")		# frantic exclimation!

# ~~~~~~~~~~~~~~~~~ ChatBot Setup ~~~~~~~~~~~~~~
#chatbot = ChatBot("D3MA") 		# Desktop Extended Mobility Assistant

exit_conditions = ("quit", "exit")

# ~~~~~~~~~~~~~ Droid Speech ~~~~~~~~~~
r2.speak("eo")		# loading

# ~~~~~~~~~~~~~~~~~ Pin Deffiintions ~~~~~~~~~~~~~~

# Analog Name, Pins & Voltage:
# AIN0-4, P1_19/P1_21/P1_23/P1_25/P1_27, 1.8v MAX
# AIN5, P2_35, 3.3v MAX
# AIN6, P1_02, 3.3v MAX
# AIN7, P2_36, 1.8v MAX

#UART.setup("/dev/ttys0", 9600)  # RX,TX pins P1_30 and P1_32 /dev/tty01  (SPI0 Pins CLK, MISO)
#UART.setup("PB-UART1")  # RX,TX pins P2_05 and P2_07 /dev/ttyO4


# ~~~~~~~~ Arduino Communications Port ~~~~~~~~
#arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

serArd = serial.Serial(port="/dev/ttys0", 9600)  # ttys0 GPIO14-TX, GPIO15-RX
serArd.close()
serArd.open()


# ~~~~~~~~ Nano-pi Serial Communications Port ~~~~~~~
#serpi = serial.Serial(port="/dev/tty2",
#                      baudrate=9600)
#serpi.close()
#serpi.open()

# ~~~~~~~~~~~~~ Droid Speech ~~~~~~~~~~
r2.speak("eeo")		# loading

# ~~~~~~~~~~~~~ AI Setup - Linux x86-x64 ~~~~~~~~~~~~

model = Model(r'/home/debian/AI-linux/modules/EN')  # Module folder
recognizer = KaldiRecognizer(model, 16000)  # No WakeWord
# recognizer = KaldiRecognizer(model, 16000, '["robot", "[unk]"]')        # WakeWord = robot ... unk = unknown command (everything else)

#sound_start_lis = vlc.MediaPlayer(r'/home/debian/AI-linux/audio/computerbeep_44.mp3')
#sound_stop_lis = vlc.MediaPlayer(r'/home/debian/AI-linux/audio/computerbeep_43.mp3')
#sound_open = vlc.MediaPlayer(r'/home/debian/AI-linux/audio/computerbeep_44.mp3')

# ~~~~~~~~~~~~~ Droid Speech ~~~~~~~~~~
r2.speak("eeo")		# loading

# ~~~~~~~~~~~~~~ Name & Location Settings ~~~~~~~~~~~~

user = "Dan"			# Owners Name
SN = "D 3 M A"			# Robot Name (D3MA) (Desktop 3xtended Mobility Assistant)
city = "Exeter"


# ~~~~~~~~~~~~~~ Memory Settings ~~~~~~~~~~
listening = bool(True)

filename = 'memories.txt'


def save_value(input_value, filename):
    with open(filename, 'w') as f:
        f.write(input_value)

def load_value(filename):
    with open(filename, 'r') as f:
        read = f.read()
    return read

try:
    value = ast.literal_eval(load_value(filename))
    print('Loading Values:', values)
except:
    print('Creating Memories File')
    values = {"SN = D 3 M A", "user = Dan",}

#if input == 'user':
#    values = 
#    save_value(str(values), filename)

# ~~~~~~~~~~~~~ Droid Speech ~~~~~~~~~~
r2.speak("eeo")		# loading more

# ~~~~~~~~~~~~~~ TTS Setup ~~~~~~~~~~~~~~~~

engine = pyttsx3.init()

rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', rate-15)  # speed of speech

volume = engine.getProperty('volume')
engine.setProperty('volume', volume+2.5)

print(f"Speech Rate : ", rate, " Volume: ", volume,)
# ~~~~~~~~~~~~~ Droid Speech ~~~~~~~~~~
r2.speak("eeeo")		# loading

voices = engine.getProperty("voices")

#engine.setProperty('voice', voices[12].id)  # male voice..  12 sounds scottish, 10 is very robotic
#engine.setProperty('voice', ('english_rp+f2'))  # female voice.. gets annoying after a while
engine.setProperty('voice', ('english'))


#for voice in voices:
#  print("ID: %s" % voice.id)
#  print("Name: %s" % voice.name)
#  print("Age: %s" % voice.age)
#  print("Gender: %s" % voice.gender)
#  print("Languages Known: %s" % voice.languages)

def output(audio):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("CPU:",f"{str(psutil.cpu_percent())}%","|","BATT:","-NILL-","|")
    print("D3MA @", datetime.datetime.now().strftime("%H:%M"), end=': ')
    print(audio)  # For printing out the output
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    engine.say(audio)
    engine.runAndWait()


# ~~~~~~~~~~~~~ Droid Speech ~~~~~~~~~~
r2.speak("eeeo")  # loading

# ~~~~~~~~~~~~~~ Recognize from Mic ~~~~~~~~~~~~ change device index depending on mirophone

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, input_device_index=1, channels=1, rate=44100, input=True,
                  frames_per_buffer=8192) # can also use rate=16000
stream.start_stream()

# ~~~~~~~~~~~~~ Droid Speech ~~~~~~~~~~
r2.speak("ooo")		# done/complete

#~~~~~~~~~~~~~~~ Power-on Self Test (POST) ~~~~~~~~~~~~~~~~~
#TBD
#
#
#

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Command Definitions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def greet():

    hour = datetime.datetime.now().hour
    if (hour >= 0) and (hour < 12):
        r2.speak("abg")
        sleep(1)
        output(f"Good Morning, I am {SN}, It is " +
               datetime.datetime.now().strftime("%H:%M"))
    elif (hour >= 12) and (hour < 18):
        r2.speak("tfs")
        sleep(1)
        output(f"Good afternoon, I am {SN}, It is " +
               datetime.datetime.now().strftime("%H:%M"))
    elif (hour >= 18) and (hour < 24):
        r2.speak("qaef")
        sleep(1)
        output(f"Good Evening, I am {SN}, It is " +
               datetime.datetime.now().strftime("%H:%M"))


def convertTime(seconds):				# function returning time in hh:mm:ss
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def idea():
    output("What would you like me to remember?")
    dataidea = recognizer.Result().title()
    output(f"I will remember this for you {user}: " + dataidea)
    with open("ideas.txt", "a", encoding="utf-8") as r:
        print(dataidea, file=r)


def weather():

    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]    # weather condition
    temp2 = res["main"]["temp"]                 # temperature in C
    output(
        f"Temperature in {city} is {format(temp2)} degrees Celsius and the condition is: {format(temp1)}")


def reboot():
    output("Rebooting subroutines")
    ti.sleep(1)  # 1 second delay
    r2.speak("ooo")
    os.system("python3 ~/roco-vosk.py")
    exit()

def reboot_system():
    output("Rebooting Base Hardware")
    ti.sleep(1)  # 1 second delay
    r2.speak("ooo")
    os.system("systemctl reboot")


def shutdown():
    hour = datetime.datetime.now().hour
    if (hour > 21) and (hour < 6):
        output("Shutting down Interface, Good night")
    else:
        output("Powering down")
    os.system('systemctl poweroff')
    
def asleep():    
    sleeping = True
    listening = False


def status():

    if listening == True:
        listening_status = "ENABLED"

    if listening == False:
        listening_status = "OFFLINE"

    total, used, free = shutil.disk_usage("/")

    disk_total = (total // (2**30))
    disk_used = (used // (2**30))
    disk_free = (free // (2**30))


#    output(f"CPU speed is {str(psutil.cpu_freq(percpu=False).current)}Mhz.")
    output(f"CPU is using: {str(psutil.cpu_percent())} % at 1Ghz. ")
    output(f"Battery is: -ERROR- . Battery Monitor NOT Connected. ") 
    output(f"Speech Recognition Subroutines are: {listening_status}. ")
    output(f"Internal Storage has: {disk_free}Gigabytes free of: {disk_total}Gigabytes total.")
    output(f"Wifi is: ENABLED and: CONNECTED.") 

   # {str(battery.percent)}%, giving {str(int(battery.secsleft))} seconds of operation remaining.")


# ~~~~~~~~~~~~~~~~~~~~ Commands: ~~~~~~~~~~~~~~~~~~~~~~~~~~
def commands(query):
    querycli = query

    if ("lon" in query):
        output("Speech Recognition Subrutines: ACTIVATED")
        listening = True

    elif ("loff" in query):
        output("Speech Recognition Subrutines: DEACTIVATED")
        listening = False

    elif ("reboot" in query):
        reboot()

    elif ("cancel" in query):
        output("Canceling Request")
        recognizer.Reset()

   
    elif ("sleep" in query):
        r2.speak("jboo")
        asleep()


    elif ("time" in query):
        output("It is currently " +
            datetime.datetime.now().strftime("%H:%M") + f"in {city}")

    elif ("date" in query):
        output("Today is day: " + str(datetime.datetime.now().day)
            + ". of month: " + str(datetime.datetime.now().month)
            + ". of the year: " + str(datetime.datetime.now().year))

    elif ("weather" in query):
        weather()


    elif ("joke" in query):
        output(pyjokes.get_joke())


    elif ("how are you" in query):
        status()


    elif ("status" in query):
        status()


    elif ("are you there" in query):
        output(f"Yes I'm here, I was just thinking about this joke, {str(pyjokes.get_joke())}")


    elif ("your name" in query):
        output(f"My name is {SN} ")


    elif ("who are you" in query):
        output(f"My name is {SN}. I am a DanDroid, made by Dans Designs. You can find him on Github")

    elif ("what can you do" in query):
        output(
            f"I am able to do many things, I can Play and Pause media, Search the web for you, take notes and compose emails, open youtube videos, and what ever else you program me to do.")
        

    # more commands here:

    else:
        #output(f"{chatbot.get_response(query)}")
        output(f"Sorry I dont understand")
        
    if query in exit_conditions:
       # shutdown AI
       sys.exit()



def controller():
    dataserblu = serblu.readline(1)  # read from bluetooth (size of bytes to read)

def write_read(x):
    dataduino = arduino.readline()
    return data

# ~~~~~~~~~~~~~ Main Code ~~~~ Run Once ~~~~~~~~~~~~~~~~~
# print python version
print("~~~~~~~~~~~~~~~~~~~~~")
print("D3MA - Digital 3xtended Mobility Assistant")
print("~~~~~~~~~~~~~~~~~~~~~")
print("Python Version: " + sys.version)

print("~~~~~~~~~~~~~~~~~~~~~")
print("Power-On Time: " + datetime.datetime.now().strftime("%H:%M"))

if serArd.isOpen():
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("Body Connection Open")
    print("~~~~~~~~~~~~~~~~~~~~~")



hour = datetime.datetime.now().hour
if (hour >= 0) and (hour < 12):
    r2.speak("abg")
    sleep(1)
    output(f"Good Morning, I am {SN}, It is " +
           datetime.datetime.now().strftime("%H:%M"))
elif (hour >= 12) and (hour < 18):
    r2.speak("tfs")
    sleep(1)
    output(f"Good afternoon, I am {SN}, It is " +
           datetime.datetime.now().strftime("%H:%M"))
elif (hour >= 18) and (hour < 24):
    r2.speak("qaef")
    sleep(1)
    output(f"Good Evening, I am {SN}, It is " +
           datetime.datetime.now().strftime("%H:%M"))


# ~~~~~~~~~~~~~ Main Code ~~~~ Loop the following ~~~~~~~

listening = True     # initial Awake state after power-on
sleeping = False

while True:

# ~~~~~~~~~~~~~~~~~~~~ Wait for Wakeword: ~~~~~~~~~~~~~~~~~~~~~~~~~~

    datawake = stream.read(6192, exception_on_overflow=False)
    wake = recognizer.Result()
    
    query = input(f"[Listening] {user}: ")
    commands(query)

    if recognizer.AcceptWaveform(datawake):
        # print("Recognized")
        print(wake)

# ~~~~~~~~~~~~~~~~~~ Wake Word: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if ("deema" in wake):	# Wake Command

        r2.speak("bj") 

        #end_time = datetime.datetime.now() + timedelta(seconds=10)  # triggers 10 second timer
        #while datetime.datetime.now() < end_time:
        listening = True  # triggers listening state for command input

    if ("robot" in wake):	# Wake Command

        r2.speak("bj")

        #end_time = datetime.datetime.now() + timedelta(seconds=10)  # triggers 10 second timer
        #while datetime.datetime.now() < end_time:
        listening = True  # triggers listening state for command input
        

    if ("computer" in wake):	# Wake Command

        r2.speak("bj")

        #end_time = datetime.datetime.now() + timedelta(seconds=10)  # triggers 10 second timer
        #while datetime.datetime.now() < end_time:
        listening = True  # triggers listening state for command input

# ~~~~~~~~~~~~~~~~~~~~ While Awake, Listen for Command: ~~~~~~~~~~~~~~~~~~~~~~~~~~
    while listening == True & sleeping == False:

        datacmd = stream.read(8192, exception_on_overflow=False)
        query = recognizer.Result()

        if recognizer.AcceptWaveform(datacmd):
            print(query)
            recognizer.Reset()


            commands(query)

        querycli = input(f"[Waiting..] {user}: ")
        commands(querycli)
# ~~~~~~~~~~~~~~~~~~~~ While Awake, wait for Command: ~~~~~~~~~~~~~~~~~~~~~~~~~~
    while sleeping == False & listening == False:

        query = input(f"[Listening Off] {user}: ")
        commands(query)

# ~~~~~~~~~~~~~~~~~~ Sleeping: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    while sleeping == True & listening == False:

        awake = input("D3MA_[sleeping]:")		# wait for input from keyboard

        if awake == '#':				# wake up key = "#"
            greet()
            sleeping = False
            listening = True

    #output(f"{chatbot.get_response(query)}")
    #print(f"{chatbot.get_response(query)}")


#controller()




# except Exception as e:
#    raise e
# finally:
print("cleanup")
GPIO.output(mypin, GPIO.LOW)
spi0.close()
spi1.close()
GPIO.cleanup()

# ~~~~~~~~~~~~~~ EOF ~~~~~~~~~~~~~
