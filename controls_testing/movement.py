
import time
import RPi.GPIO as GPIO


# Set motor to high and delay by moving time
def move_forward(WHEEL_MPS, DEFAULT_DISTANCE, in1, in2):
    moving_time = DEFAULT_DISTANCE / WHEEL_MPS
    GPIO.output(in1, True)
    GPIO.output(in2, True)
    time.sleep(moving_time)
    GPIO.output(in1, False)
    GPIO.output(in2, False)


# Move forwards by a certain amount every time, stochastically

if __name__ == "__main__":

    # Distance between chairs, in meters
    DEFAULT_DISTANCE = 1

    # Speed of wheels, measured in meters per second
    WHEEL_MPS = .2

    # Total distance traveled
    DISTANCE_TRAVELED = 0

    # Setup GPIO pins
    in1 = 16
    in2 = 18

    # Setup GPIO interface
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)

    GPIO.output(in1, False)
    GPIO.output(in2, False)

    DEFAULT_DISTANCE = int(input(f"Enter seat distance (DEFAULT = {DEFAULT_DISTANCE}): ") or DEFAULT_DISTANCE)

    print(input)

    move_forward(WHEEL_MPS, DEFAULT_DISTANCE, in1, in2)