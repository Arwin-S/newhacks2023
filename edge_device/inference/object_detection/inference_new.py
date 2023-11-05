from ultralytics import YOLO

# print('he')
import cv2 as cv

# Nano
model = YOLO('yolov8n.pt')

cam = cv.VideoCapture(0)

i = 0

while True:

    # Debugging
    # print(i)
    # i+=1

    ret,frame = cam.read()

    cv.namedWindow("Webcam Frame", cv.WINDOW_NORMAL)

    results = model(frame, show=True, conf=0.4, save=False)

    if cv.waitKey(1) == ord('q'):
        break
