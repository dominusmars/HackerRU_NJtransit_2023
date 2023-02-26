import cv2
import requests
import numpy as np

class Client:
    def __init__(self, api_url, buffer_size=28672):
        self.url = api_url
        self.buffer_size = buffer_size
    def get_video_stream(self):
        # Send a request to the video stream URL and read the response stream
        response = requests.get(self.url, stream=True)
        byt = bytes()

        # Loop over the response stream and yield each video frame
        for chunk in response.iter_content(chunk_size=self.buffer_size):
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

    def move(self):
        response = requests.post(self.url+"/move_camera")
        return response.text

    def moveCamera(self):
        response = requests.post(self.url+"/move_forward")
        return response.text

    def turn_around(self):
        response = requests.post(self.url+"/turn_around")
        return response.text
