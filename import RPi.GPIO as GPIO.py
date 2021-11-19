import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
sostoyanie = GPIO.input(14)
i = 0
while True:
    if (sostoyanie == 0 and GPIO.input(14) == 0):
        i = not i
        GPIO.output(15, i)
        time.sleep(0.5)
    sostoyanie = GPIO.input(14)    
