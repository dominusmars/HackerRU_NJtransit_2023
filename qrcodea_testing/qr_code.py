import cv2
import numpy as np
import zbarlight
from PIL import Image


# Initialize the webcam
cap = cv2.VideoCapture(1)
# Keep reading frames from the webcam until the user quits
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: could not capture image from webcam")
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Print the shape and data type of the grayscale image
    print("Shape:", gray.size)
    print("Data type:", gray.dtype)
    if len(gray.shape) != 2:
        print("Error: grayscale image has invalid shape:", gray.shape)
        break

    new_image =pil_img = Image.fromarray(gray)
    # Decode any QR codes in the frame
    qr_codes = zbarlight.scan_codes(['qrcode'], new_image)

    # If any QR codes were found, print them out
    if qr_codes is not None:
        for code in qr_codes:
            print(code.decode('utf-8'))

    # Display the frame in a window
    cv2.imshow('QR Code Scanner', frame)

    # Wait for the user to press a key
    key = cv2.waitKey(1)

    # If the user presses the 'q' key, quit the program
    if key == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
