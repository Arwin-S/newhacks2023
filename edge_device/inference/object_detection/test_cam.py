import cv2
import time

camera_index = 0  # or 1, 2, etc. if you have multiple cameras
cam = cv2.VideoCapture(camera_index)

# Set camera resolution (optional, try removing if you get errors)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Check if the camera was opened successfully
if not cam.isOpened():
    print(f"Cannot open camera {camera_index}")
    exit()

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cam.read()

        # If frame is read correctly, ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('Camera Test', frame)

        # Wait for 1ms. If 'q' is pressed, exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

        # Sleep for a bit to allow camera to adjust
        # time.sleep(0.1)
finally:
    # When everything is done, release the capture
    cam.release()
    cv2.destroyAllWindows()
