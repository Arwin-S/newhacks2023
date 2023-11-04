from ultralytics import YOLO

import cv2 as cv

# YOLO v8 Nano
model = YOLO('yolov8n.pt')

# Webcam
cam = cv.VideoCapture(1)

i = 0

while True:

    # Debugging
    # print(i)
    # i+=1

    ret,frame = cam.read()

    cv.namedWindow("Webcam", cv.WINDOW_NORMAL)

    results = model(frame, show=True, conf=0.4, save=False)

    if cv.waitKey(1) == ord('q'):
        break

# SKU110K dataset
# model.train(data='custom.yaml', epochs=3)

# Run env
# env/Scripts/Activate.ps1
