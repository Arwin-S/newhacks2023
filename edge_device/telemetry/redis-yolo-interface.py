import redis
import time
import random
from datetime import datetime
import random
from matplotlib import pyplot as plt
import seaborn as sns
from yolo import Yolo
from gpiozero import AngularServo
import math
import pygame


# initial setups
pygame.init()
screen_size = 400

surface = pygame.display.set_mode((screen_size, screen_size)) # window size and pixels width/height
line_length = screen_size // 2
pos1 = pygame.Vector2(screen_size//2, screen_size//2)


servo = servo =AngularServo(18, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)
servo.angle = 0

sweep_angle = 0

if __name__ == "__main__":

    # Database Credentials
    host = 'redis-15344.c99.us-east-1-4.ec2.cloud.redislabs.com'
    port = 15344
    password = ''

    # Interfacing
    redis_client = redis.StrictRedis(
        host=host, port=port, password=password, db=0)

    ts = redis_client.ts()

    # try:
    #     ts.delete("det", "-", "+")
    # except Exception as e:
    #     print("")

    percepter = Yolo()

    while True:
        surface.fill((0, 0, 0))  # erase surface memory before we draw new things
        

        if servo.angle == 0:
            x_cos = screen_size // 2
            y_sin = 0
            servo.angle = 90
        elif servo.angle == 90:
            x_cos = 0
            y_sin = screen_size // 2
            servo.angle = 180
        elif servo.angle == 180:
            x_cos = (-1 * (screen_size // 2))
            y_sin = 0
            servo.angle = 270
        elif servo.angle == 270:
            x_cos = 0
            y_sin = (-1 * (screen_size // 2))
            servo.angle = 0
        time.sleep(0.5)



        # x_cos = line_length * (math.cos(servo.angle))
        # y_sin = line_length * (math.sin(servo.angle))

        x_final = screen_size//2 + x_cos
        y_final = screen_size//2 + (-1 * y_sin)

        pos2 = pygame.Vector2(x_final, y_final)

        pygame.draw.circle(surface, "green", pos1, 20)
        pygame.draw.circle(surface, "green", pos1, 100, 1)
        pygame.draw.circle(surface, "green", pos1, 200, 1)
        #pygame.draw.circle(surface, "green", pos1, 350, 1)

        # pygame.draw.line(surface, "green", pos1,pos2, 2)

        print("Current angle for the radar sweep: ", servo.angle)

        for i in range(128):
            x_cos2 = line_length * (math.cos((servo.angle - 90) - (0.0025 * i)))
            y_sin2 = line_length * (math.sin((servo.angle - 90) - (0.0025 * i)))

            x_final2 = screen_size//2 + x_cos2
            y_final2 = screen_size//2 + (-1 * y_sin2)

            pos3 = pygame.Vector2(x_final2, y_final2)

            pygame.draw.line(surface, (0,(255 - 2*i) ,0), pos1,pos3, 2)

        percepter.take_img()
        output = percepter.infer()
        # print(type(output))
        print("CAM HEADING: ", servo.angle)
        # print("SWEEP HEADING: ", sweep_angle)

        if "person" in output:
            # DRAW CIRCLE at cam angle

            x_cos3 = line_length * (math.cos(servo.angle))
            y_sin3  = line_length * (math.sin(servo.angle))

            x_final3 = screen_size//2 + (x_cos3)//2
            y_final3 = screen_size//2 + (-1 * (y_sin3)//2)

            pos_p = pygame.Vector2(x_final3, y_final3)

            pygame.draw.circle(surface, "red", pos_p, 20)


        for class_name, count in output.items():
            print(class_name, count)
            ts.add(class_name, "*", count)
