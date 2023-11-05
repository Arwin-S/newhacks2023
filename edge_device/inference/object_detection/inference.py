from ultralytics import YOLO
import torch
import cv2 as cv

# YOLO v8 Nano
model = YOLO('best.pt')

print("loaded")

# Webcam
# cam = cv.VideoCapture(1, cv.CAP_DSHOW)
cam = cv.VideoCapture(1, cv.CAP_DSHOW)

i = 0

while True:

    # Debugging
    # print(i)
    # i+=1

    ret,frame = cam.read()

    results = model(frame, show=True, conf=0.4, save=False, classes=0)

    if cv.waitKey(1) == ord('q'):
        break

# print("Length")
# print(len(results))

count = 0

for r in results:
    boxArr = r.boxes.xyxy

boxArrDim = boxArr.shape

print(boxArrDim[0])


# SKU110K dataset
# model.train(data='custom.yaml', epochs=3)

# Run env
# env/Scripts/Activate.ps1
