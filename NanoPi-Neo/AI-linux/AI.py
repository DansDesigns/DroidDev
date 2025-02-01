from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import datetime
import time as ti
import os
import psutil
import clipboard
import pyautogui
import pyjokes
import pywhatkit
import requests
import smtplib
import webbrowser as we
from email.message import EmailMessage
# from newsapi import NewsApiClient
# from secrets import senderemail, password
from time import sleep
from pynput.keyboard import Key, Controller
import wikipedia
import random
import vlc


# ~~~~~~~~~~~~~ Initial Setup ~~~~~~~~~~~~
battery = psutil.sensors_battery()
model = Model(r'/home/pi/Vosk_AI_Linux/modules/EN')  #  Module folder
recognizer = KaldiRecognizer(model, 16000)                               # No WakeWord
#recognizer = KaldiRecognizer(model, 16000, '["robot", "[unk]"]')        # WakeWord = robot ... unk = unknown command (everything else)
sound_start_lis = vlc.MediaPlayer(r'/home/pi/Vosk_AI_Linux/audio/computerbeep_44.mp3')
sound_stop_lis = vlc.MediaPlayer(r'/home/pi/Vosk_AI_Linux/audio/computerbeep_43.mp3')
sound_open = vlc.MediaPlayer(r'/home/pi/Vosk_AI_Linux/audio/computerbeep_44.mp3')
# ~~~~~~~~~~~~~~ Name Settings ~~~~~~~~~~~~

user = "Daniel"
SN= "computer"

greetings = ['Yes', 'Hello', '0110?', 'Whats on', 'Hi']

# ~~~~~~~~~~~~~~ TTS Setup ~~~~~~~~~~~~~~~~

engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 180)     # speed of speech
print(f"Speech Rate : ", rate)
voices = engine.getProperty("voices")
#engine.setProperty("voice", voices[12].id)     # male voice
engine.setProperty('voice',('english_rp+f2'))      # female voice

def output(audio):
    print(datetime.datetime.now().strftime("%I:%M"), end = ' ')

   # if battery.power_plugged:
    #    print("CHRG:", battery.percent,"%", end = ' ')

#    else:
 #       print("DRAIN", battery.percent,"%", end = ' ')

    print(audio) # For printing out the output
    engine.say(audio)
    engine.runAndWait()

# ~~~~~~~~~~~~~~ Recognize from Mic ~~~~~~~~~~~~

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# ~~~~~~~~~ Keyboard Simulation ~~~~~~~

keyboard = Controller()

# Example of use:
# keyboard.press('a')
# keyboard.release('a')

# Win Key:
# keyboard.press(Key.cmd)
# keyboard.release(Key.cmd)

# To Copy & Paste:
# keyboard.press(Key.ctrl)
# keyboard.press('c')
# keyboard.release('c')
# keyboard.release(Key.ctrl)

# F11 Key:
# keyboard.press(Key.f11)

# For getting the device index you can execute this code So if you want to change the device you can do that.
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(
#         index, name))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Command Definitions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def greet():
    hour = datetime.datetime.now().hour
    if (hour >= 0) and (hour < 12):
        output(f"Good Morning {user}, It is " +
               datetime.datetime.now().strftime("%I:%M"))
    elif (hour >= 12) and (hour < 18):
        output(f"Good afternoon {user}, It is " +
               datetime.datetime.now().strftime("%I:%M"))
    elif (hour >= 18) and (hour < 24):
        output(f"Good Evening {user}, It is " +
               datetime.datetime.now().strftime("%I:%M"))

# function returning time in hh:mm:ss

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

#def batt():
#    output(f"My battery is at {str(battery.percent)}%")
#    if battery.power_plugged:
#        print("Charging: ", battery.percent)
#    else:
#        print("Not Charging", battery.percent, "%")
#        print("Discharge time ", int(battery.secsleft), "seconds of operation remaining")
#        # converting seconds to hh:mm:ss
#        print("Battery left : ", convertTime(battery.secsleft))

def savechanges():
    output("Saving Changes..")
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.ctrl)

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
    os.system("python main.py")
    exit()


def shutdown():
    hour = datetime.datetime.now().hour
    if (hour > 21) and (hour < 6):
        output(f"Good Night {user}! Have a nice Sleep")
    else:
        output(f"Shutting down now..")
    quit()




# ~~~~~~~~~~~~~ Main Code ~~~~ Run Once ~~~~~~~~~~~~~~~~~

greet()

# ~~~~~~~~~~~~~ Main Code ~~~~ Loop the following ~~~~~~~



while True:
    datawake = stream.read(8192, exception_on_overflow = False)
    wake = recognizer.Result()
    if recognizer.AcceptWaveform(datawake):
        print(recognizer.Result())
        #print(wake)

    if (f"{SN}" in wake):
        sound_start_lis.play()
        ti.sleep(0.7)  # 1 second delay
        sound_start_lis.stop()
        listening = True
        output(random.choice(greetings))
        print(datetime.datetime.now().strftime("%I:%M"), "<LISTENING..>")

        while listening:
            datacmd = stream.read(8192, exception_on_overflow=False)
            query = recognizer.Result()
            if recognizer.AcceptWaveform(datacmd):
                print(query)
                recognizer.Reset()

            if ("time" in query):
                output("It is currently " +
                datetime.datetime.now().strftime("%I:%M"))
                listening = False


            elif ("date" in query):
                output("Today is " + str(datetime.datetime.now().day)
                       + " " + str(datetime.datetime.now().month)
                       + " " + str(datetime.datetime.now().year))
                listening = False


            elif ("weather" in query):
                weather()
                listening = False

            elif ("read" in query):
                output(clipboard.paste())
                listening = False

            elif ("joke" in query):
                output(pyjokes.get_joke())
                listening = False

            elif ("idea" in query):
                idea()
                listening = False

            elif ("remind me" in query):
                ideas = open("ideas.txt", "r")
                output(f"You told me to remember these ideas:\n{ideas.read()}")
                output("That's all I have.")
                listening = False

            elif ("screenshot" in query):
                pyautogui.screenshot(str(ti.time()) + ".png").show()
                listening = False

            elif ("how are you" in query):
                output(f"I'm good, my Cpu is running at 2.8GHz, with a load of {str(psutil.cpu_percent())}%.")
                listening = False


            elif ("are you there" in query):
                output(f"Yes I'm here, I was just thinking about this joke, {str(pyjokes.get_joke())}")
                listening = False

            elif ("your name" in query):
                output(f"My name is {SN} ")
                listening = False

            elif ("who are you" in query):
                output(f"My name is {SN}, and I am an Artificial Intelligence programed by Dan's Droids for use in Robots.")
                listening = False

            elif ("full screen" in query):
                keyboard.press(Key.f11)
                output(f"Fullscreen Toggled")
                listening = False

            elif ("pause media" in query):
                output(f"Paused")
                keyboard.press(Key.media_play_pause)
                listening = False

            elif ("resume media" in query):
                output("Resuming..")
                keyboard.press(Key.media_play_pause)
                listening = False

            elif ("what can you do" in query):
                output(
                    f"I am able to do many things, I can Play and Pause media, Search the web for you, take notes and compose emails, open youtube videos, and what ever else you program me to do.")

                listening = False


            elif ("shut down" in query):
                shutdown()
                listening = False


            elif ("reboot" in query):
                reboot()
                listening = False

            elif ("Hello" in query):
                greet()
                listening = False

            elif ("save file" in query):
                output("Changes Saved")
                savechanges()
                listening = False


            elif ("cancel" in query):
                output("Canceling Request")
                recognizer.Reset()
                listening = False

            elif ("search for" in query):


                try:
                    print(query)
                    query.replace("search for", "")
                    search_for = query
                    Web_result = wikipedia.summary(search_for)
                    output("Searching for answers")
                    output(Web_result)
                    listening = False
                except (KeyboardInterrupt):
                    engine.stop()

        print(datetime.datetime.now().strftime("%I:%M"), "<LISTENING STOPPED>")
        sound_stop_lis.play()
        ti.sleep(0.7)  # 1 second delay
        listening = False
        sound_stop_lis.stop()