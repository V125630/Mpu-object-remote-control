import  serial
import RPi.GPIO as GPIO
from time import sleep
from servo import servo


servoX = servo(8)
servoY = servo(10)

servoX.Startservo()
servoY.Startservo()


while True:
    try: 
        with serial.Serial('/dev/ttyACM0', 19200, timeout=.2) as ser:
            line = ser.readline()   # read a '\n' terminated line
            line = line.decode("utf-8").strip()
            print(line)
            line1 = line.split()
            x = float(line1[0])
            y = float(line1[1])
            servoY.Cdc2(y)
            servoX.Cdc2(x)
            sleep(0.2)

    except:
       print("no movement")
       sleep(.2)

