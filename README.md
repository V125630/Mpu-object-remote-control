# object-remote-control

## Description
control two servo from a raspberi pie from an mpu.




## External  libraries: <br>
- pySerial https://github.com/pyserial/pyserial 

<br>

## Set Up
install pySerial on raspberi pie with pip install pyserial<br>
connect mpu to paspberi pie
<br>
identify the com port of the mpu and update the serial port on line 16 of servo_control.py
<br>
connect servox pwm lead from servo to raspberi pie gpio pin8
<br>
connect servoy pum lead from servo 2 to raspberi pie gpio pin10
<br>
run the code and move the mpu for results.