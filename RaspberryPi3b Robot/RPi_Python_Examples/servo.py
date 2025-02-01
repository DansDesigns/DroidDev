# Servo Controlled via PocketBeagle by DansDesigns
#
#
#
#
#
#

# ~~~~~~~~~~~~  Libraries: ~~~~~~~~~~~~~~
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

# ~~~~~~~~~~~~  Setup Servos: ~~~~~~~~~~~~~~
servo_1 = "P2_01"
servo_2 = "P2_03"
#servo_3 = "P1_36"
#servo_4 = "P1_33"

# ~~~~~~~~~~~~  Calibrate Servos: ~~~~~~~~~~~~~~
PWM.start(servo_1, 50,60)
PWM.start(servo_2, 50,60)
#PWM.start(servo_3, 50,60)
#PWM.start(servo_4, 50,60)

sleep(1)

PWM.stop(servo_1)
PWM.stop(servo_2)
#PWM.stop(servo_3)
#PWM.stop(servo_4)

PWM.cleanup()


while True:

    # Rotate the servo CCW 180 degrees
    PWM.start(servo_1,0,60)
    sleep(1)
    PWM.stop(servo_1)
    PWM.cleanup()
    
    # Rotate the servo CW 180 degrees
    PWM.start(servo_1,50,60)
    sleep(1)
    PWM.stop(servo_1)
    PWM.cleanup()


#~~EOF~~
