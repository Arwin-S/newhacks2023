from PIL import Image, ImageDraw
import numpy as np
import tflite_runtime.interpreter as tflite
import time

input_img_path = 'test.jpg'

# Parameters
BATCH_SIZE = 1
HEIGHT = 640
WIDTH = 640
CHANNELS = 3

def load_img():
    # Load the image
    image = Image.open(input_img_path)

    # Resize image to match model's expected input
    image = image.resize((WIDTH, HEIGHT))

    # Convert image to numpy array
    image_array = np.array(image)

    # Check if the image is already in the correct format
    if image_array.shape == (HEIGHT, WIDTH, CHANNELS):
        # Add a batch dimension
        input_data = np.expand_dims(image_array, axis=0).astype(np.float32)
    else:
        # Incorrect image format, handle the error
        raise ValueError(f"Image has incorrect shape: {image_array.shape}, expected: {(HEIGHT, WIDTH, CHANNELS)}")

    # Check if the input data's shape matches the model's input shape
    if input_data.shape == (BATCH_SIZE, HEIGHT, WIDTH, CHANNELS):
        print("Input data is ready for the model.")
    else:
        raise ValueError(f"Input data has incorrect shape: {input_data.shape}, expected: {(BATCH_SIZE, HEIGHT, WIDTH, CHANNELS)}")

    return input_data

def draw_boxes(image, boxes, scores, classes):
    draw = ImageDraw.Draw(image)
    for box, score, class_id in zip(boxes, scores, classes):
        y_min, x_min, y_max, x_max = box
        left, right, top, bottom = x_min * image.width, x_max * image.width, y_min * image.height, y_max * image.height
        draw.rectangle([left, top, right, bottom], outline="red", width=2)
        draw.text((left, top), f"{class_id} {score:.2f}", fill="red")
    image.save('yolo_with_boxes.jpg')
    image.show()

def decode_output(output_data, num_classes=80):
    # Decode the output following the YOLO output format
    # This is a placeholder function. You would need to replace this with the actual decoding logic
    # that applies sigmoid to the relevant parts of the tensor to get scores and bounding boxes,
    # and then use non-maximum suppression to filter the boxes.
    boxes = []
    scores = []
    classes = []
    for i in range(output_data.shape[2]):
        row = output_data[0, :, i]
        x, y, width, height = row[:4]
        confidence = row[4]
        class_scores = row[5:]
        class_id = np.argmax(class_scores)
        if confidence > 0.5:  # Placeholder threshold
            boxes.append((y, x, y + height, x + width))  # Box format: y_min, x_min, y_max, x_max
            scores.append(confidence)
            classes.append(class_id)
    print("boxes num: ", len(boxes))
    return boxes, scores, classes

if __name__ == "__main__":
    interpreter = tflite.Interpreter(model_path='yolov8n_saved_model/yolov8n_float16.tflite')
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_data = load_img()

    if input_data.shape != tuple(input_details[0]['shape']):
        raise ValueError(f"Input data shape {input_data.shape} does not match model's expected input shape {tuple(input_details[0]['shape'])}")

    interpreter.set_tensor(input_details[0]['index'], input_data)
    start = time.time()
    interpreter.invoke()
    end = time.time()
    print("time for inference: ", end - start)

    output_data = interpreter.get_tensor(output_details[0]['index'])
    boxes, scores, classes = decode_output(output_data)

    # Now let's draw the boxes on the image
    image = Image.open(input_img_path)
    draw_boxes(image, boxes, scores, classes)
