import statistics as stat
import matplotlib.pyplot as plt
import numpy as np
import math

def readJetData(filename):
    with open(filename) as f:
        lines = f.readlines()

    steps = 0
    count = 0
    dataLineIndex = 0

    for index, line in enumerate(lines):
        if line[0] != '-' and line[0] != '\n':
            dataLineIndex = index
            break

        if 'steps' in line:
            words = line.split()
            for word in words:
                try:
                    steps = float(word)
                except ValueError:
                    pass

        if 'count' in line:
            words = line.split()
            for word in words:
                try:
                    count = int(word)
                except ValueError:
                    pass

    dataLines = lines[dataLineIndex:]
    data = np.asarray(dataLines, dtype=float)

    return data, steps, count


steps = [0]*8
count = [0]*8
data0, steps[0], count[0] = readJetData("00 mm.txt")
data1, steps[1], count[1] = readJetData("10 mm.txt")
data2, steps[2], count[2] = readJetData("20 mm.txt")
data3, steps[3], count[3] = readJetData("30 mm.txt")
data4, steps[4], count[4] = readJetData("40 mm.txt")
data5, steps[5], count[5] = readJetData("50 mm.txt")
data6, steps[6], count[6] = readJetData("60 mm.txt")
data7, steps[7], count[7] = readJetData("70 mm.txt")
data0 = 0.16*data0 - 158.42
data1 = 0.16*data1 - 158.42
data2 = 0.16*data2 - 158.42
data3 = 0.16*data3 - 158.42
data4 = 0.16*data4 - 158.42
data5 = 0.16*data5 - 158.42
data6 = 0.16*data6 - 158.42
data7 = 0.16*data7 - 158.42



print('введите давление в трубке Пито без потока, целое число')
davl = int(input())
data0 = 2/1.2*(data0-davl)
data0 = np.fabs(data0)
data0 = np.sqrt(data0)

data1 = 2/1.2*(data1-davl)
data1 = np.fabs(data1)
data1 = np.sqrt(data1)

data2 = 2/1.2*(data2-davl)
data2 = np.fabs(data2)
data2 = np.sqrt(data2)

data3 = 2/1.2*(data3-davl)
data3 = np.fabs(data3)
data3 = np.sqrt(data3)

data4 = 2/1.2*(data3-davl)
data4 = np.fabs(data4)
data4 = np.sqrt(data4)

data5 = 2/1.2*(data5-davl)
data5 = np.fabs(data5)
data5 = np.sqrt(data5)

data6 = 2/1.2*(data6-davl)
data6 = np.fabs(data6)
data6 = np.sqrt(data6)

data7 = 2/1.2*(data7-davl)
data7 = np.fabs(data7)
data7 = np.sqrt(data7)

x = np.linspace(-5,5, int(count[0]))
plt.title("Скорость потока воздуха в сечении затопленной струи") # заголовок
plt.xlabel("Положение трубки Пито относительно центра струи [мм]")         # ось абсцисс
plt.ylabel("Скорость воздуха [м/с]")    # ось ординат
plt.grid()              # включение отображение сетки
plt.plot(x , data0,'r',x , data1,'g',x , data2,'b',x , data3,'y',x , data4,'c',x , data5,'m',x , data6,'k',x , data7,'goldenrod')

plt.legend(loc = 'upper right')
plt.legend(['Q(00мм)','Q(10мм)','Q(20мм)','Q(30мм)','Q(40мм)','Q(50мм)','Q(60мм)','Q(70мм)'])

plt.savefig("Скорость потока воздуха в сечении затопленной струи.png")