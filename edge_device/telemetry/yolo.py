from ultralytics import YOLO
import time
import cv2 as cv
from time import sleep

class Yolo:
    def __init__(self) -> None:
        self.model = YOLO('yolov8n.pt')
        self.img = None
        self.cam = cv.VideoCapture(0)


    def take_img(self):
        _, self.img = self.cam.read()


    def infer(self):
        output = self.model(self.img, show=False, save=False) 
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