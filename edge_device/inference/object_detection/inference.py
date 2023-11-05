from ultralytics import YOLO
import torch
import cv2 as cv

# YOLO v8 Nano
model = YOLO('best.pt')

print("loaded")

# Webcam
cam = cv.VideoCapture(0)


while True:

    ret,frame = cam.read()

    results = model(frame, show=True, conf=0.4, save=False)

    if cv.waitKey(1) == ord('q'):
        break

# print("Length")
# print(len(results))

# for r in results:
#     boxArr = r.boxes.xyxy

# boxArrDim = boxArr.shape

# print(boxArrDim[0])

# SKU110K dataset
# model.train(data='custom.yaml', epochs=3)

# Run env
# env/Scripts/Activate.ps1
