import time
from qrcode import qr_functions
from client import client
from image_recognition import faces_functions
import cv2
import numpy as np
import math

url = "http://192.168.212.151:5000"

# Initialize variables
detect_people = False
next_step_move = False
get_ticket = False
move_froward = False
turn_camera_180 = False
sent = False
process_frame = False
passengers = 0
passengers_this_round = -1
tickets_this_round = 0
average_this_round = []
parse_amount = 40

cl = client.Client(url)


# Define a function to reset variables for a new round
def reset_round():
    global frames_parse
    frames_parse = 0
    global passengers_this_round
    passengers_this_round = 0
    global tickets_this_round
    tickets_this_round = 0
    global average_this_round
    average_this_round = []


# Define a function to initialize movement
def init():
    global move_froward
    move_froward = True


# Define the main function
def main():
    global move_froward
    global detect_people
    global average_this_round
    global passengers_this_round
    global get_ticket
    global passengers
    global sent
    global cl
    global process_frame
    init()
    # Loop over each frame from the video stream
    for frame in cl.get_video_stream():
        if not process_frame:
            cv2.imshow("Video Stream", frame)
            process_frame = True
            continue

        # Find bodies in the current frame using image recognition
        if not get_ticket:
            bodies = faces_functions.find_bodies(frame)

            # Draw the bodies on the frame for visualization
            final_frame = faces_functions.draw_bodies_on_frame(frame, bodies)

            # Display the final frame
            cv2.imshow("Video Stream", final_frame)
        else:
            cv2.imshow("Video Stream", frame)

        # Check if it's time to move forward
        if move_froward:
            if not sent:
                cl.display("Going to next row")
                cl.move_forward(1)
                time.sleep(4)
                sent = True
            move_froward = False
            reset_round()
            detect_people = True
            sent = False
            continue

        # Check if it's time to detect people
        if detect_people:
            if not sent:
                print("scanning ...")
                cl.display("Scanning ...")
                sent = True

            # Keep track of the number of bodies detected in each frame
            if len(average_this_round) >= parse_amount:
                passengers_this_round = math.ceil(np.average(average_this_round))
                if passengers_this_round == 0:
                    print("No Passengers Detected")
                    sent = False
                    detect_people = False
                    move_froward = True
                    reset_round()
                    continue
                detect_people = False
                get_ticket = True
                passengers = passengers + passengers_this_round
                print("Passengers detected:", passengers_this_round)
                print("Total of Passengers:", passengers)
                sent = False
                continue
            number_of_bodies = len(bodies)
            average_this_round.append(number_of_bodies)

        # Check if it's time to get a ticket
        if get_ticket:
            if not sent:
                cl.display("Tickets Please ...")
                sent = True

            if qr_functions.identify_qr_codes(frame):
                get_ticket = False
                if next_step_move:
                    cl.display("Thank you", 1)
                    time.sleep(3)
                    move_froward = True
                    sent = False
                else:
                    cl.display("Thank you", 1)
                    time.sleep(3)
                    cl.move_camera()
                    reset_round()
                    detect_people = True
                    sent = False

        # Wait for a key press and check if it's the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
