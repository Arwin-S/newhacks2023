from ultralytics import YOLO
import cv2 as cv
import time

# Nano
print("hello")
model = YOLO('yolov8n.pt')

cam = cv.VideoCapture(0)
print("hello passed vc")
cam.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while True:

    ret,frame = cam.read()
    # If frame is read correctly, ret is True
    # if not ret:
    #     print("Can't receive frame (stream end?). Exiting ...")
    #     break
    
    # cv.imshow('Camera Test', frame)

    results = model(frame, show=True, conf=0.4, save=False)

    if cv.waitKey(1) == ord('q'):
        break

    # time.sleep(0.1)

# SKU110K dataset
# model.train(data='custom.yaml', epochs=3)

# Run env
# env/Scripts/Activate.ps1
