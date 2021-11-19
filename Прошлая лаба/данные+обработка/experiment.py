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
data0 = 0.164*data0 - 136
data1 = 0.164*data1 - 136
data2 = 0.164*data2 - 136
data3 = 0.164*data3 - 136
data4 = 0.164*data4 - 136
data5 = 0.164*data5 - 136
data6 = 0.164*data6 - 136
data7 = 0.164*data7 - 136



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

data4 = 2/1.2*(data4-davl)
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



x = np.linspace(-5.6,5.6, int(count[0]))

v0 = round(np.mean(data0),3)
v1 = round(np.mean(data1),3)
v2 = round(np.mean(data2),3)
v3 = round(np.mean(data3),3)
v4 = round(np.mean(data4),3)
v5 = round(np.mean(data5),3)
v6 = round(np.mean(data6),3)
v7 = round(np.mean(data7),3)

q0 = round(3.14 * 0.0095**2 / 4 * 1.2 * v0*1000,3)
q1 = round(3.14 * 0.0095**2 / 4 * 1.2 * v1*1000,3)
q2 =round(3.14 * 0.0095**2 / 4 * 1.2 * v2*1000,3)
q3 = round(3.14 * 0.0095**2 / 4 * 1.2 * v3*1000,3)
q4 = round(3.14 * 0.0095**2 / 4 * 1.2 * v4*1000,3)
q5 = round(3.14 * 0.0095**2 / 4 * 1.2 * v5*1000,3)
q6 = round(3.14 * 0.0095**2 / 4 * 1.2 * v6*1000,3)
q7 = round(3.14 * 0.0095**2 / 4 * 1.2 * v7*1000,3)



plt.title("Скорость потока воздуха в сечении затопленной струи") # заголовок
plt.xlabel("Положение трубки Пито относительно центра струи [мм]")         # ось абсцисс
plt.ylabel("Скорость воздуха [м/с]")    # ось ординат
plt.figure(figsize=(12, 10))
plt.grid()              # включение отображение сетки
plt.plot(x , data0,'r',x , data1,'g',x , data2,'b',x , data3,'y',x , data4,'c',x , data5,'m',x , data6,'k',x , data7,'goldenrod')

plt.legend(loc = 'upper right')
plt.legend(['Q(00мм) = %f  [г/c]'%q0  ,'Q(10мм) = %f  [г/c]'%q1  ,'Q(20мм) = %f  [г/c]'%q2  ,'Q(30мм) = %f  [г/c]'%q3  ,'Q(40мм) = %f  [г/c]'%q4  ,'Q(50мм) = %f  [г/c]'%q5  ,'Q(60мм) = %f  [г/c]'%q6  ,'Q(70мм) = %f  [г/c]'%q7  ,])

plt.savefig("Скорость потока воздуха в сечении затопленной струи.png")