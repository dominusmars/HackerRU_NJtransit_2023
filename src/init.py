from qrcode import qr_functions
from client import client 
from image_recognition import faces_functions
import cv2
import numpy as np

detect_people = False
next_step_move = False
get_ticket = False
move_froward = False
turn_camera_180 = False
passengers = 0
passengers_this_round = -1
tickets_this_round = 0
average_this_round = []
parse_amount = 20

def reset_round():
    global average_this_round
    average_this_round = -1
    global frames_parse
    frames_parse = 0
    global passengers_this_round
    passengers_this_round = 0
    global tickets_this_round
    tickets_this_round = 0
    global average_this_round
    average_this_round= []
  


def init():
    global move_froward
    move_froward = True;
def main():
    global move_froward
    global detect_people
    global average_this_round
    global passengers_this_round
    global get_ticket
    global passengers
    init()
    for frame in client.get_video_stream(url):
        bodies = faces_functions.find_bodies(frame)
        final_frame = faces_functions.draw_bodies_on_frame(frame, bodies)

        cv2.imshow('Video Stream', final_frame)

        if(move_froward):
            client.move()
            move_froward = False
            reset_round()
            detect_people = True
            continue
        if(detect_people):
            if(len(average_this_round)  >= parse_amount):
                detect_people = False
                get_ticket = True
                passengers_this_round = np.average(average_this_round)
                passengers = passengers + passengers_this_round
                print("Passengers detected:  "+ passengers_this_round)
                print("Total of Passengers: "+ passengers)
                continue
            number_of_bodies = len(bodies)
            average_this_round.append(number_of_bodies)
        if(get_ticket):
            if(qr_functions.identify_qr_codes(frame)):
                get_ticket = False
               
                if(next_step_move):
                    move_froward = True
                else:
                    client.moveCamera(turn_camera_180)
                    turn_camera_180 = not turn_camera_180
                    reset_round()
                    detect_people = True



        # Wait for a key press and check if it's the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    url = 'http://192.168.212.151:5000/video_feed'

   