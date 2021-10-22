import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
led = [21, 20, 16, 12, 7, 8, 25, 24]
bits = len(dac)
levels = 2**bits
troyka = 17
comp = 4
i = 0 # Счетчик времени при зарядке
j = 0 # Счетчик времени при разрядке
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
    while i != 2800: # Пока счетчик не достигнет значения 2800 считываем значения напряжения и заносим в список napr
        i = i + 1
        adc()
    GPIO.output(17, GPIO.LOW)
    while j != 3200: # Пока счетчик не достигнет значения 3200 считываем значения напряжения и заносим в список napr
        j = j + 1
        adc1()
    
    napr1 = [str(item) for item in napr] # элементы списка napr преобразуем в строки
    with open("data.txt", "w") as f: # создаем файл со значениями напряжения
         f.write("\n".join(napr1))

    T = np.linspace(0, 60, num = 6000) # создаем массив времени 
    
    dats_array = np.loadtxt("data.txt", dtype=int)

    dats_array = 3.3 / 256 * dats_array

    fig, ax = plt.subplots(figsize=(16,10), dpi =400)
    ax.plot(T, dats_array, label = 'линия интерполяции', markevery = 125, marker = '.', markersize = 15) # передаем в качестве аргументов функции plot массив времени и массив значений времени
    ax.set_xlabel('t, c')
    ax.set_ylabel('U(t), В')
    ax.set_title("Зависимость напряжения на конденсаторе от времени")
    ax.legend()
    ax.grid()

    plt.text(10, 1.25, "Время зарядки 28 с; разрядки - 32 с", fontsize=15)

    ax.minorticks_on()


    ax.grid(which='major',
        color = 'k', 
        linewidth = 2)

    ax.grid(which='minor', 
        color = 'k', 
        linestyle = ':')

    fig.savefig("1.svg")
    fig.savefig("1.png")
    plt.show()
    

finally:
    GPIO.cleanup(led)
    GPIO.cleanup(dac)