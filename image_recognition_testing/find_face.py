import cv2

def find(frame):
    body_cascade = cv2.CascadeClassifier('/xml/haarcascade_profileface.xml')
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect lower body in the frame
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=1,
                                           minSize=(10, 20), maxSize=(3000, 6000))