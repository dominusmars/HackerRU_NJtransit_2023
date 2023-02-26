import pickle
import socket
import struct

import cv2

HOST = '0.0.0.0'
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn, addr = s.accept()
print('connected to client:',addr)
data = b'' ### CHANGED
payload_size = struct.calcsize("Q") ### CHANGED

while True:

    # Retrieve message size
    while len(data) < payload_size:
        data += conn.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0] ### CHANGED
    print("recieved msg of size:", msg_size)
    # Retrieve all data based on message size
    while len(data) < msg_size:
        data += conn.recv(4096)
        print("building message",len(data),"of:",msg_size)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Extract frame
    frame = pickle.loads(frame_data)
    print("attempt display")
    # Display
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
