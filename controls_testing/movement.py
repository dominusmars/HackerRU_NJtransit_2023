
import time
import RPi.GPIO as GPIO

# Set motor to high and delay by moving time
def move_forward(WHEEL_MPS, DEFAULT_DISTANCE, in1, in2):
    moving_time = DEFAULT_DISTANCE / WHEEL_MPS

    GPIO.output(in1, GPIO.HIGH)
    print("on")

    time.sleep(moving_time)

    GPIO.output(in1, GPIO.LOW)
    print("off")

# Move forwards by a certain amount every time, stochastically

if __name__ == "__main__":

    # Distance between chairs, in meters
    DEFAULT_DISTANCE = 1

    # Speed of wheels, measured in meters per second
    WHEEL_MPS = .2

    # Setup GPIO pin
    in1 = 16

    # Setup GPIO interface
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)

    # Set default state to LOW
    GPIO.output(in1, GPIO.LOW)

    # DEFAULT_DISTANCE = int(input(f"Enter seat distance (DEFAULT = {DEFAULT_DISTANCE}): ") or DEFAULT_DISTANCE)

    move_forward(WHEEL_MPS, DEFAULT_DISTANCE, in1, in2)
