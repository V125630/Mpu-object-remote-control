import RPi.GPIO as GPIO
from time import sleep

class servo():
    """
    sets up a servo

    ## servo_pin is the pwm pin the servo is plugged into
    
    
    """
    def __init__(self,servo_pin):
        servo_pin = servo_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(servo_pin, GPIO.OUT)
        self.pwm=GPIO.PWM(servo_pin, 50)
        self.pwm.start(0)
        self.xlocal = 6.0

    def Startservo(self):
        """ set duty to 90 degrees"""
        self.pwm.ChangeDutyCycle(self.xlocal)    

    def Cdc2(self,value ):
        """ChangeDutyCycle from mpu checking for input of 1, 0 , -1 for left 
        no movement and right"""
        xlocal = self.xlocal
        x = value
        duty = 0.0
        if x == -1.0:
            xlocal = xlocal - 0.5
            duty = xlocal

        if x == 0.0:
            xlocal = xlocal
            duty = 0.0

        if x == 1.0:
            xlocal = xlocal + 0.5
            duty = xlocal
            if xlocal >= 12 :
                xlocal = 12

        self.xlocal = xlocal
        self.pwm.ChangeDutyCycle(duty)

    def Cdc(self,value ):
        """ChangeDutyCycle"""
        self.pwm.ChangeDutyCycle(value)

        

    def closepwm(self):
        self.pwm.stop()

        


        
  


#g901 = servo(8)

# g901.pwm.ChangeDutyCycle(20)
#g901.Cdc(20)
#g901.Cdc2(1)
#g901.Cdc2(1)
#g901.Cdc2(1)
#g901.Cdc2(1)

# g902 = servo(10)

# g902.Cdc(11)
# g902.Cdc(20)
#g901.closepwm()
#g902.closepwm()