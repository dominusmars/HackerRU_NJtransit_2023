import cv2
import requests
import numpy as np

def get_video_stream(url, buffer_size=28672):
    # Send a request to the video stream URL and read the response stream
    response = requests.get(url, stream=True)
    byt = bytes()

    # Loop over the response stream and yield each video frame
    for chunk in response.iter_content(chunk_size=buffer_size):
        # Append the chunk to the byte buffer
        byt += chunk

        # Find the start and end of the current video frame
        a = byt.find(b'\xff\xd8')
        b = byt.find(b'\xff\xd9')

        # If we have a complete video frame, yield it
        if a != -1 and b != -1:
            # Extract the video frame from the byte buffer
            frame_bytes = byt[a:b + 2]
            byt = byt[b + 2:]

            # Decode the video frame and yield it
            frame = cv2.imdecode(np.frombuffer(frame_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
            yield frame

def display_video_stream(url):
    # Open a window to display the video stream
    cv2.namedWindow('Video Stream', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video Stream', 640, 480)

    # Loop over the video frames from the video stream and display each frame
    for frame in get_video_stream(url):
        cv2.imshow('Video Stream', frame)

        # Wait for a key press and check if it's the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up the window and exit
    cv2.destroyAllWindows()

def main():
    # Define the URL of the video stream
    url = 'http://192.168.212.151:5000/video_feed'

    # Display the video stream from the URL
    display_video_stream(url)

if __name__ == '__main__':
    main()