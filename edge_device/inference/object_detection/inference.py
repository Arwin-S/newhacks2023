from ultralytics import YOLO
import cv2
import time


model = YOLO('yolov8n.pt')

img = cv2.imread('yolo.jpg')

# First run to 'warm-up' the model
model.predict(source=img, save=False, save_txt=False, conf=0.5, verbose=False)

# # Second run
t_start = time.monotonic()
results = model.predict(source=img, save=False, save_txt=False, conf=0.5, verbose=False)
dt = time.monotonic() - t_start
print("dT:", dt)

# Show results
boxes = results[0].boxes
names = model.names
confidence, class_ids = boxes.conf, boxes.cls.int()
rects = boxes.xyxy.int()
for ind in range(boxes.shape[0]):
    print("Rect:", names[class_ids[ind].item()], confidence[ind].item(), rects[ind].tolist())