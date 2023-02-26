from qrcode import qr_functions
from client import client 
from image_recognition import faces_functions
import cv2
if __name__ == '__main__':
    url = 'http://192.168.212.151:5000/video_feed'

    for frame in client.get_video_stream(url):
        cv2.imshow('Video Stream', frame)

        # Wait for a key press and check if it's the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break