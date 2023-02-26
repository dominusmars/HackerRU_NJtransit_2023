import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

re = 16
GPIO.setup(re, GPIO.OUT)

while (True):
    GPIO.output(re, GPIO.LOW)
    time.sleep(2)
    GPIO.output(re, GPIO.HIGH)
    time.sleep(2)
