#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# last edit 08/03/2023
#
# Roco Robot Companion
# NanoPi Neo
#
# PIP Packages:
#
# pip3 install ttastromech
# pip3 install adafruit-circuitpython-pca9685
# pip3 install pyserial
# pip3 install pyaudio
# pip3 install HC-05-ConfigTool
#
#
#
# Linux Dependant Packages:
#
# sudo apt-get install build-essential python3-dev python3-pip portaudio19-dev python3-all-dev -y
#
#

# Imports:
from vosk import Model, KaldiRecognizer
import sys
import time
import serial
import pyaudio
import pyttsx3
import datetime
import time as ti
import os
import psutil
#import clipboard
import pyjokes
import requests
import smtplib
import webbrowser as we
from email.message import EmailMessage
from time import sleep
import wikipedia
import random
import vlc    # python-vlc
from ttastromech import TTAstromech
import subprocess
import socket
import shutil





# ~~~~~~~~~~~~~ Main Setup ~~~~~~~~~~~~
r2 = TTAstromech()


# ~~~~~~~~ HC-05 Bluetooth Port ~~~~~~~~


# ~~~~~~~~ Nano pi Serial Communications Port ~~~~~~~


# ~~~~~~~~~~~~~ AI Setup - Linux x86-x64 ~~~~~~~~~~~~

model = Model(r'/home/pi/AI-linux/modules/EN')  # Module folder
recognizer = KaldiRecognizer(model, 16000)  # No WakeWord
# recognizer = KaldiRecognizer(model, 16000, '["robot", "[unk]"]')        # WakeWord = robot ... unk = unknown command (everything else)
sound_start_lis = vlc.MediaPlayer(r'/home/pi/AI-linux/audio/computerbeep_44.mp3')
sound_stop_lis = vlc.MediaPlayer(r'/home/pi/AI-linux/audio/computerbeep_43.mp3')
sound_open = vlc.MediaPlayer(r'/home/pi/AI-linux/audio/computerbeep_44.mp3')

# ~~~~~~~~~~~~~~ Name Settings ~~~~~~~~~~~~

user = "Daniel"
SN = "computer"

# ~~~~~~~~~~~~~~ TTS Setup ~~~~~~~~~~~~~~~~

engine = pyttsx3.init()

rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 198)  # speed of speech
print(f"Speech Rate : ", rate)
voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[12].id)     # male voice
engine.setProperty('voice', ('english_rp+f2'))  # female voice


def output(audio):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("CPU:",f"{str(psutil.cpu_percent())}%","|","BATT:","-NILL-","|")
    print("D3MA @", datetime.datetime.now().strftime("%H:%M"), end=': ')
    print(audio)  # For printing out the output
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    engine.say(audio)
    engine.runAndWait()


# ~~~~~~~~~~~~~~ Recognize from Mic ~~~~~~~~~~~~

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, input_device_index=1, channels=1, rate=44100, input=True,
                  frames_per_buffer=8192)
stream.start_stream()


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

# function returning time in hh:mm:ss

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def idea():
    output("What would you like me to remember?")
    data = recognizer.Result().title()
    output("I will remember this for you: " + data)
    with open("ideas.txt", "a", encoding="utf-8") as r:
        print(data, file=r)


def weather():
    city = "Exeter"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    output(
        f"Temperature in {city} is {format(temp2)} degrees Celsius and it is {format(temp1)}")


def reboot():
    output(f"Rebooting...")
    ti.sleep(1)  # 1 second delay
    os.system("python3 ~/roco.py")
    exit()


def shutdown():
    hour = datetime.datetime.now().hour
    if (hour > 21) and (hour < 6):
        output(f"Good Night {user}! Have a nice Sleep")
    else:
        output(f"Shutting down now..")
    os.system('systemctl poweroff')

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
        


#dataser1 = ser.readline(1)  # read from bluetooth (size of bytes to read)

# ~~~~~~~~~~~~~ Main Code ~~~~ Run Once ~~~~~~~~~~~~~~~~~
print("~~~~~~~~~~~~~~~~~~~~~")
print("D3MA - Digital 3xtended Mobility Assistant")
print("~~~~~~~~~~~~~~~~~~~~~")
print("Python Version: " + sys.version)
print("~~~~~~~~~~~~~~~~~~~~~")
print("Power-On Time: " + datetime.datetime.now().strftime("%H:%M"))
print("~~~~~~~~~~~~~~~~~~~~~")

greet()


print("~~~~~~~~~~~~~~~~~~~~~")
print(datetime.datetime.now().strftime("%H:%M") + " D3MA - Waiting for Wake Word...")
print("~~~~~~~~~~~~~~~~~~~~~")

# ~~~~~~~~~~~~~ Main Code ~~~~ Loop the following ~~~~~~~


try:
    while True:
        # ~~~~~~~~~~~~~ Main Code ~~~~ Console Input ~~~~~~~
        #query = input(f"[Listening] {user}: ")
        #commands(query)
        
        # ~~~~~~~~~~~~~ Main Code ~~~~ Engage AI ~~~~~~~
        datawake = stream.read(6192, exception_on_overflow=False)
        wake = recognizer.Result()
        if recognizer.AcceptWaveform(datawake):
            print(recognizer.Result())
        # ~~~~~~~~~~~~~~~~~~ Wake Word: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # NEW RECOGNISER SETTINGS WITH NESTED COMMANDS

        if (f"{SN}" in wake):
            #sound_start_lis.play()
            #ti.sleep(0.7)  # 1 second delay
            #sound_start_lis.stop()
            print("~~~~~~~~~~~~~~~~~~~~~")
            print(datetime.datetime.now().strftime("%H:%M") + " D3MA - Listening...")
            print("~~~~~~~~~~~~~~~~~~~~~")

            end_time = datetime.datetime.now() + timedelta(seconds=5)  # triggers 10 second timer
            while datetime.datetime.now() < end_time:
                listening = True  # triggers listening state for command input

            # ~~~~~~~~~~~~~~~~~~~~ While Awake, Listen for Command: ~~~~~~~~~~~~~~~~~~~~~~~~~~

                while listening:
                    datacmd = stream.read(6192, exception_on_overflow=False)
                    query = recognizer.Result()
                    if recognizer.AcceptWaveform(datacmd):
                        print(query)
                        recognizer.Reset()
                        commands(query)


        print("~~~~~~~~~~~~~~~~~~~~~")
        print(datetime.datetime.now().strftime("%H:%M") + " D3MA - Waiting for Wake Word...")
        print("~~~~~~~~~~~~~~~~~~~~~")
        #print(datetime.datetime.now().strftime("%I:%M"), "<LISTENING STOPPED>")
        sound_stop_lis.play()
        ti.sleep(0.7)  # 1 second delay
        listening = False
        #sound_stop_lis.stop()



except Exception as e:
    raise e
finally:
    print("cleanup")
# EOF


