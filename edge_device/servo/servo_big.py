from gpiozero import AngularServo
from time import sleep

servo =AngularServo(18, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)
pause = 1
servo.angle = 0
while (True):
    servo.angle = 10
    sleep(pause)

    servo.angle = 30
    sleep(pause)

    servo.angle = 50
    sleep(pause)

    servo.angle = 70
    sleep(pause)

    servo.angle = 90
    sleep(pause)

    servo.angle = 110
    sleep(pause)

    servo.angle = 130
    sleep(pause)

    servo.angle = 150
    sleep(pause)

    servo.angle = 170
    sleep(pause)

    servo.angle = 190
    sleep(pause)

    servo.angle = 210
    sleep(pause)

    servo.angle = 230
    sleep(pause)


    servo.angle = 250
    sleep(pause)


    servo.angle = 270
    sleep(pause)



