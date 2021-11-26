import matplotlib.pyplot as plt
import numpy as np
import math

#Калибровка1
with open ("00 Pa.txt") as f:
    s = f.readlines()
    values = []
    for line in s:
        if line[0] != '-' and line[0] != '\n':
            values.append(int(line.split()[0]))
    summ = sum(values)
    sr = round(summ/len(values))
    print ("Среднее значение показателей АЦП при 0 Па: ", sr )

with open ("max Pa.txt", "r") as f2:
    s2 = f2.readlines()
    values2 = []
    for line in s2:
        if line[0] != '-' and line[0] != '\n':
            values2.append(int(line.split()[0]))
    summ2 = sum(values2)
    sr2 = round(summ2/len(values2))
    print("Среднее значение показателей АЦП при 110 Па: ", sr2)

k = round(110/abs(sr2-sr), 3)
print('Коэффициент калибровки давления:', k)
b=-round(sr*k, 3)
print('Калибровочное уравнение: ', 'P =', k, '* x', b )


fig, ax = plt.subplots(figsize=(16,10), dpi=400)
acp = np.linspace(sr, sr2)
pressure = k*acp+b


zavis = 'P' + ' ' + '=' + str(k) + '*' + 'x' + str(b)

ax.plot(pressure, acp, 'green', linewidth = '1.0', label = zavis)

ax.set_xlim([min(pressure), 1.1*max(pressure)])
ax.set_ylim([min(acp), 1.1*max(acp)])

plt.title("Калибровочный график зависимости показаний АЦП  от давления", fontstyle = 'italic', horizontalalignment = 'center')
plt.xlabel("Давление, Па")
plt.ylabel("Отсчёты АЦП")

plt.legend()

plt.grid(which='major', color='gray', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', color='gray', linestyle='--', linewidth = 0.25)


plt.minorticks_on()

fig.savefig("pressure-calibration.png")


plt.show()

#Калибровка2
st = [0, 880]
sm = [0, 4.5]
ks = (sm[1] - sm[0]) / (st[1] - st[0])
print(ks)
fig, ax = plt.subplots(figsize=(16,10), dpi=400)
ax.plot(sm, st, "gray", linewidth = '1.0', label = "X = {0:.1e} * step [м]".format(ks / 100))

ax.set_xlim([min(sm), 1.1*max(sm)])
ax.set_ylim([min(st), 1.1*max(st)])

plt.title("Зависимость перемещения трубки Пито от шага двигателя", fontstyle = 'italic', horizontalalignment = 'center')
plt.xlabel("Перемещение трубки Пито, см")
plt.ylabel("Количество шагов")

plt.legend()
plt.grid(which='major', color='green', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', color='green', linestyle='--', linewidth = 0.25)

plt.minorticks_on()

fig.savefig("distance-calibration.png")
plt.show()

# Обработка
def readfile(file):
    with open(file) as f:
        lines = f.readlines()
    steps = 0
    count = 0

    datas = []

    for i, line in enumerate(lines):
        if line[0] != '-' and line[0] != '\n':
            datas.append(float(line[0]))
        if 'steps' in line:
            for step in line.split():
                try:
                    steps = float(step)
                except:
                    pass

        if 'count' in line:
            for c in line.split():
                try:
                    count = int(c)
                except ValueError:
                    pass
        data = np.asarray(datas, dtype=float)
        data = 0.346*data-286.142
        data = 2 / 1.2 * (data - 110)
        data = np.fabs(data)
        data = np.sqrt(data)
        v = round(np.mean(data), 3)
        q = round(3.14 * 0.005 ** 2  * 1200 * v, 6)
    return data, steps, count, v, q

steps = [0]*8
count = [0]*8
data0, steps[0], count[0], v0, q0 = readfile("00 mm.txt")
data1, steps[1], count[1], v1, q1 = readfile("10 mm.txt")
data2, steps[2], count[2], v2, q2 = readfile("20 mm.txt")
data3, steps[3], count[3], v3, q3 = readfile("30 mm.txt")
data4, steps[4], count[4], v4, q4 = readfile("40 mm.txt")
data5, steps[5], count[5], v5, q5 = readfile("50 mm.txt")
data6, steps[6], count[6], v6, q6 = readfile("60 mm.txt")
data7, steps[7], count[7], v7, q7 = readfile("70 mm.txt")


x = np.linspace(-3, 3, 190)

fig, ax = plt.subplots(figsize=(16,10), dpi=400)
ax.plot(x, data0, 'r')
ax.plot(x, data1, 'g')
ax.plot(x, data2, 'blue')
ax.plot(x, data3, 'black')
ax.plot(x, data4, 'm')
ax.plot(x, data5, 'y')
ax.plot(x, data6, 'orange')
ax.plot(x, data7, 'purple')



plt.title("Скорость потока воздуха в сечении затопленной струи", fontstyle = 'italic', horizontalalignment = 'center')
plt.xlabel("Положение трубки Пито относительно центра струи [мм]")
plt.ylabel("Скорость воздуха [м/с]")
labels = ['Q(00 мм) = ' + str(q0) + ' [г/c]','Q(10 мм) = ' + str(q1) + ' [г/c]', 'Q(20 мм) = ' + str(q2) + ' [г/c]', 'Q(30 мм) = ' + str(q3) + ' [г/c]', 'Q(40 мм) = ' + str(q4) + ' [г/c]', 'Q(50 мм) = ' + str(q5) + ' [г/c]', 'Q(60 мм) = ' + str(q6) + ' [г/c]', 'Q(70 мм) = ' + str(q7) + ' [г/c]',]
print(labels)
plt.legend(labels)
plt.grid(which='major', color='green', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', color='green', linestyle='--', linewidth = 0.25)

plt.minorticks_on()

fig.savefig("velocity-outgo.png")
plt.show()

fig, ax = plt.subplots(figsize=(16,10), dpi=400)

distance = [0, 10, 20, 30, 40, 50, 60, 70]
q = [q0, q1, q2, q3, q4, q5, q6, q7]


ax.plot(distance, q, "m", linewidth = '1.0')

ax.set_xlim([min(distance), 1.1*max(distance)])
ax.set_ylim([min(q), 1.0005*max(q)])

plt.title("Зависимость расхода газа от расстояния до сопла", fontstyle = 'italic', horizontalalignment = 'center')
plt.xlabel("Расстояние от сопла, мм")
plt.ylabel("Расход газа, [г/c]")


plt.grid(which='major', color='green', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', color='green', linestyle='--', linewidth = 0.25)


plt.minorticks_on()

fig.savefig("q.png")


plt.show()