import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxU = 3.3
troyka = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def dec2bin (value):
    return [int(bin) for bin in bin(value)[2:].zfill(bits)]

def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    for value in range(256):
        signal = bin2dac(value)
        voltage = value / levels * maxU
        time.sleep(0.001)
        compValue = GPIO.input(comp)
        if compValue == 0:
            print (Divalue, signal, voltage)
            break


try:
    while True:
        adc()    
finally:
    GPIO.cleanup(dac. GPIO.LOW)
    GPIO.cleanup(dac)

