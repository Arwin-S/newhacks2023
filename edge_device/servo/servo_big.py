from gpiozero import AngularServo
from time import sleep

servo =AngularServo(18, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)
pause = 3
servo.angle = 0
while (True):
    servo.angle = 0
    print("0/360")
    sleep(pause)

    servo.angle = 90
    print("90")
    sleep(pause)

    servo.angle = 270
    print("270")
    sleep(pause)

