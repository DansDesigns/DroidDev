#    L9110s Python Code for NanoPi Neo v1.4
#    Combined with UART Code for HC-05 Bluetooth on UART1
#
#    uses RPI.GPIO_NP from https://github.com/friendlyarm/RPi.GPIO_NP
#    also uses pyserial
#
# to install:
# sudo apt-get update
# sudo apt-get install python-dev
# git clone https://github.com/friendlyarm/RPi.GPIO_NP
# cd RPi.GPIO_NP
# python setup.py install                 
# sudo python setup.py install
#    
#    
#    
#    
##r2.speak("ybe")    # greeting
#r2.speak("ooo")    # done/complete/finished
#r2.speak("eo")    # loading
#r2.speak("eeo")    # loading more
#r2.speak("oops")    # oops
#r2.speak("hjk")    # buzz exclimation
#r2.speak("qwerty")    # frantic exclimation!

#~~~~~~~~~ Imports ~~~~~~~~~~~~~~~
import serial,time
from time import sleep
import RPi.GPIO as GPIO
from ttastromech import TTAstromech
r2 = TTAstromech()

#~~~~~~~~~ UART Settings ~~~~~~~~~~

ser = serial.Serial(port = "/dev/ttyS1", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
    print ("BCC is open")    #BCC Bluetooth Controller Connection
    r2.speak("bcc")


#~~~~~~~~~ Motor Deffinitions ~~~~~~
    
# Motor A = Left
# Motor B = Right
# Pin Number, NOT Linux GPIO Number
ain1 = 13
ain2 = 15
bin1 = 16
bin2 = 18

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
    #
       data = ser.readline(1)    # read from bluetooth (size of bytes rt read)

       #if data:    # if data is present from bluetooth
           #print(data.decode("utf-8"))    # print data to console.remove \r\n line endings

       if data.decode("utf-8") == "B":
           print("Brake")
           stop()

       elif data.decode("utf-8") == "S":
           print("back") 
           back()

       elif data.decode("utf-8") == "A":  
           print("left") 
           left()

       elif data.decode("utf-8") == "D":
           print("right")
           right()

       elif data.decode("utf-8") == "C":
           print("C-Button")

       elif data.decode("utf-8") == "W":   
           print("forward") 
           forward()
           #r2.speak("hjk")
           
       else: stop()


GPIO.cleanup()
ser.close()
# EOF

