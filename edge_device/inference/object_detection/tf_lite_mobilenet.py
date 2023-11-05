import cv2
import numpy as np
import tflite_runtime.interpreter as tflite

# Load TFLite model and allocate tensors.
interpreter = tflite.Interpreter(model_path="ssd_mobilenet_v1_1_metadata_1.tflite")
interpreter.allocate_tensors()

# Get model info
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the image to required size and type
    input_shape = input_details[0]['shape']
    input_frame = cv2.resize(frame, (input_shape[1], input_shape[2]))
    input_frame = np.expand_dims(input_frame, axis=0)
    # No need to normalize, just convert to uint8
    input_frame = input_frame.astype(np.uint8)


    # Perform the actual detection by running the model with the image as input
    interpreter.set_tensor(input_details[0]['index'], input_frame)
    interpreter.invoke()

    # Retrieve detection results
    boxes = interpreter.get_tensor(output_details[0]['index'])[0] # Bounding box coordinates
    classes = interpreter.get_tensor(output_details[1]['index'])[0] # Class index
    scores = interpreter.get_tensor(output_details[2]['index'])[0] # Confidence

    # Loop over all detections and draw detection box if confidence is above a threshold
    for i in range(len(scores)):
        if (scores[i] > 0.5):
            # Get bounding box coordinates and draw box
            # Interpreter can return coordinates that are outside of image dimensions, need to force them to be within image using max() and min()
            ymin = int(max(1, (boxes[i][0] * frame.shape[0])))
            xmin = int(max(1, (boxes[i][1] * frame.shape[1])))
            ymax = int(min(frame.shape[0], (boxes[i][2] * frame.shape[0])))
            xmax = int(min(frame.shape[1], (boxes[i][3] * frame.shape[1])))
            
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (10, 255, 0), 2)

            # Draw label
            object_name = "Object" # you need a proper class mapping here
            label = f"{object_name}: {int(scores[i]*100)}%"
            cv2.putText(frame, label, (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
