from ultralytics import YOLO
import time
# Load a COCO-pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Display model information (optional)
# model.info()

# Run inference with the YOLOv8n model on the 'bus.jpg' image
tic = time.time()
results = model('yolo.jpg')
# print(results)
toc = time.time()

speed = toc - tic
print("inferencce time elapsed = ", speed)
# print(results.names)
if len(results) == 0:
    print("ERROR: no results!")

results = results[0]
classes = results.names
# print(classes, len(results.boxes.cls))

detected_classes = {}
for detected_class in results.boxes.cls:
    # print(classes[detected_class])

    if classes[int(detected_class.numpy())] not in detected_classes:
        detected_classes[classes[int(detected_class.numpy())]] = 1
    else:
        detected_classes[classes[int(detected_class.numpy())]] += 1

print(detected_classes, type(detected_class))
    
