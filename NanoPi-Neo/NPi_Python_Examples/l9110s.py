#    L9110s Python Code for NanoPi Neo v1.4
#    
#    uses RPI.GPIO_NP from https://github.com/friendlyarm/RPi.GPIO_NP
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
#

#~~~~~~~~~ Imports ~~~~~~~~~~~
from time import sleep
import RPi.GPIO as GPIO

#~~~~~~~~~ Deffinitions ~~~~~~
# Motor A = Left
# Motor B = Right

ain1 = 13
ain2 = 15
bin1 = 16
bin2 = 18


def forward():
    GPIO.output(ain1,True)        
    GPIO.output(ain2,False)
    GPIO.output(bin1,True)
    GPIO.output(bin2,False)
    sleep(1)
        

def back():
    GPIO.output(ain1,False)        
    GPIO.output(ain2,True)
    GPIO.output(bin1,False)
    GPIO.output(bin2,True)
    sleep(1)
        

def left():
    GPIO.output(ain1,True)        
    GPIO.output(ain2,False)
    GPIO.output(bin1,False)
    GPIO.output(bin2,True)
    sleep(1)
        

def right():
    GPIO.output(ain1,False)        
    GPIO.output(ain2,True)
    GPIO.output(bin1,True)
    GPIO.output(bin2,False)
    sleep(1)
        
def stop():
    GPIO.output(ain1,False)        
    GPIO.output(ain2,False)
    GPIO.output(bin1,False)
    GPIO.output(bin2,False)
    sleep(2)
    

#~~~~~~~~~~~ Setup ~~~~~~~~~~~~~
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ain1,GPIO.OUT)
GPIO.setup(ain2,GPIO.OUT)
GPIO.setup(bin1,GPIO.OUT)
GPIO.setup(bin2,GPIO.OUT)



#~~~~~~~~~~~ While Loop ~~~~~~~~~~~~~~
while True:
    #
    forward()
    back()
    left()
    right()
    stop()
    
    
    
gpio.cleanup()
# EOF