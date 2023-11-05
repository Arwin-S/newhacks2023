from ultralytics import YOLO

# Load a model
model = YOLO('yolov3-tinyu.pt')  # load an official model
# model = YOLO('retail.pt')  # load an official model


model.export(format='tflite')
