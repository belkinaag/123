import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
led = [21, 20, 16, 12, 7, 8, 25, 24]
bits = len(dac)
levels = 2**bits
troyka = 17
comp = 4
i = 0
j = 0
napr = [] #список, содержащий значения напряжения

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(led, GPIO.OUT, initial = GPIO.LOW)


def dec2bin (value):
    return [int(bin) for bin in bin(value)[2:].zfill(bits)]

def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    value = 0
    for i in range(8):
        value = value + 2**(7 - i)
        signal = bin2dac(value)
        time.sleep(0.001)
        compValue = GPIO.input(comp)
        if compValue == 0:
            value = value - 2**(7 - i)
            voltage = value / levels * 3.3
    GPIO.output(led, signal)
    print (value, signal, voltage)
    napr.append(value)

def adc1():
    value = 0
    for i in range(8):
        value = value + 2**(7 - i)
        signal = bin2dac(value)
        time.sleep(0.001)
        compValue = GPIO.input(comp)
        if compValue == 0:
            value = value - 2**(7 - i)
            voltage = value / levels * 3.3
    GPIO.output(led, signal)
    print (value, signal, voltage)
    napr.append(value)

try:
    while i != 2600:
        i = i + 1
        adc()
    GPIO.output(17, GPIO.LOW)
    while j != 2800:
        j = j + 1
        adc1()
    plt.plot(napr)
    plt.show()

    napr1 = [str(item) for item in napr] # элементы списка napr преобразуем в строки

    with open("data.txt", "w") as f: # создаем файл со значениями напряжения
        f.write("\n".join(napr1))
finally:
    GPIO.cleanup(led)
    GPIO.cleanup(dac)