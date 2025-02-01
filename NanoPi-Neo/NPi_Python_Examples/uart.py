import serial,time
import RPi.GPIO as GPIO



ser = serial.Serial(port = "/dev/ttyS1", baudrate=9600)	
ser.close()
ser.open()
if ser.isOpen():
    print ("Serial1 is open!")
    #ser.write("Hello World!")


while True:
     
       data = ser.readline(1)		# read from bluetooth (size of bytes rt read)

       #if data:					# if data is present from bluetooth
           #print(data.decode("utf-8"))		# print data to console.remove \r\n line endings

       if data.decode("utf-8") == "W":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           print("forward")				# print data to console

       if data.decode("utf-8") == "S":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           print("back")				# print data to console

       if data.decode("utf-8") == "A":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           print("left")				# print data to console

       if data.decode("utf-8") == "D":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           print("right")				# print data to console

       if data.decode("utf-8") == "C":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           print("C-Button")				# print data to console

       if data.decode("utf-8") == "Z":			# if data is present from bluetooth.remove \r\n and compaire the remaining
           print("Brake")				# print data to console





ser.close()
# EOF