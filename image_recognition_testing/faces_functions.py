import cv2

# Load the classifier for lower body detection
body_cascade = cv2.CascadeClassifier('/xml/haarcascade_profileface.xml')


def find_bodies(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect lower body in the frame
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=1,
                                           minSize=(10, 20), maxSize=(3000, 6000))
    return bodies

def draw_bodies_on_frame(frame, bodies):
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame