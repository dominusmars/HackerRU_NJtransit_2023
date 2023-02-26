import cv2

# Load the classifier for lower body detection
body_cascade = cv2.CascadeClassifier('/xml/haarcascade_profileface.xml')

# Open a video capture stream from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture stream
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect lower body in the frame
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=1,
                                           minSize=(10, 20), maxSize=(3000, 6000))
    
    # Draw rectangles around the detected bodies
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Show the resulting frame
    cv2.imshow('Lower body detection', frame)
    
    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture stream and close all windows
cap.release()
cv2.destroyAllWindows()
