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
import RPI.GPIO as GPIO

#~~~~~~~~~ Deffinitions ~~~~~~
# Motor A = Left
# Motor B = Right
AINA = 0
AINB = 1
BINA = 2
BINB = 3

def forward():
    GPIO.output(AINA,True)        
    GPIO.output(AINB,False)
    GPIO.output(BINA,True)
    GPIO.output(BINB,False)
    sleep(1)
        

def back():
    GPIO.output(AINA,False)        
    GPIO.output(AINB,True)
    GPIO.output(BINA,False)
    GPIO.output(BINB,True)
    sleep(1)
        

def left():
    GPIO.output(AINA,True)        
    GPIO.output(AINB,False)
    GPIO.output(BINA,False)
    GPIO.output(BINB,True)
    sleep(1)
        

def right():
    GPIO.output(AINA,False)        
    GPIO.output(AINB,True)
    GPIO.output(BINA,True)
    GPIO.output(BINB,False)
    sleep(1)
        
def stop():
    GPIO.output(AINA,False)        
    GPIO.output(AINB,False)
    GPIO.output(BINA,False)
    GPIO.output(BINB,False)
    
    

#~~~~~~~~~~~ Setup ~~~~~~~~~~~~~
GPIO.setmode(GPIO.BOARD)
GPIO.setup(AINA,GPIO.OUT)
GPIO.setup(AINB,GPIO.OUT)
GPIO.setup(BINA,GPIO.OUT)
GPIO.setup(BINB,GPIO.OUT)



#~~~~~~~~~~~ While Loop ~~~~~~~~~~~~~~
while True:
    #
    forward()
    back()
    left()
    right()
    
    
    
    
# EOF