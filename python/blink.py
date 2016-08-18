import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

while True:
    try:
        GPIO.output(25,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(25,GPIO.LOW)
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.output(25,GPIO.LOW)
        exit()
