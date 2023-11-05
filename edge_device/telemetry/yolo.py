from ultralytics import YOLO
import time
import cv2 as cv
from gpiozero import AngularServo
from time import sleep

class Yolo:
    def __init__(self) -> None:
        self.model = YOLO('yolov8n.pt')
        self.img = None
        self.cam = cv.VideoCapture(0)
        # self.servo = servo =AngularServo(18, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)
        # self.servo.angle = 0

    def take_img(self):
        _, self.img = self.cam.read()
        # if self.servo.angle == 0:
        #     self.servo.angle = 90
        # elif self.servo.angle == 90:
        #     self.servo.angle == 180
        # elif self.servo.angle == 180:
        #     self.servo.angle = 270
        # elif self.servo.angle == 270:
        #     self.servo.angle = 0

    def infer(self):
        output = self.model(self.img, show=True, save=False) 
        output = output[0]
        classes = output.names
        detected_classes = {}

        if len(output) == 0:
            print("ERROR: no outputs!")
        else:
            for detected_class in output.boxes.cls:
            # print(classes[detected_class])

                if classes[int(detected_class.numpy())] not in detected_classes:
                    detected_classes[classes[int(detected_class.numpy())]] = 1
                else:
                    detected_classes[classes[int(detected_class.numpy())]] += 1

        # print(detected_class, type(detected_class))
        return detected_classes
        # format: {'person': 15, 'chair': 3, 'dining table': 3}