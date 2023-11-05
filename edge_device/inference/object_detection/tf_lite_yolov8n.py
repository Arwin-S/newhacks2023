from ultralytics import YOLO

# Load a model
model = YOLO('yolov8m.pt') 
results = model('yolo.jpg')