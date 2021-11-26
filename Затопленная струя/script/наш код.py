import matplotlib.pyplot as plt
import numpy as np
import math
 
# def readfile(file):
#     with open(file) as f:
#         lines = f.readlines()
#     steps = 0
#     count = 0
 
#     datas = []
 
#     for i, line in enumerate(lines):
#         if line[0] != '-' and line[0] != '\n':
#             datas.append(float(line[0]))
#         if 'steps' in line:
#             for step in line.split():
#                 try:
#                     steps = float(step)
#                 except:
#                     pass
 
#         if 'count' in line:
#             for c in line.split():
#                 try:
#                     count = int(c)
#                 except ValueError:
#                     pass
#         data = np.asarray(datas, dtype=float)
#         # data = 0.346*data-286.142
#         # data = 2 * (data - 110) / 1.2
#         # data = np.fabs(data)
#         # data = np.sqrt(data)
#         # v = round(np.mean(data), 3)
#         # q = round(3.14 * 0.005 ** 2  * 1200 * v, 3)
#     return data, steps, count
 
def readfile(filename):
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
 
# steps = [0]*8
# count = [0]*8
# data0, steps[0], count[0], v0, q0 = readfile("00 mm.txt")
# data1, steps[1], count[1], v1, q1 = readfile("10 mm.txt")
# data2, steps[2], count[2], v2, q2 = readfile("20 mm.txt")
# data3, steps[3], count[3], v3, q3 = readfile("30 mm.txt")
# data4, steps[4], count[4], v4, q4 = readfile("40 mm.txt")
# data5, steps[5], count[5], v5, q5 = readfile("50 mm.txt")
# data6, steps[6], count[6], v6, q6 = readfile("60 mm.txt")
# data7, steps[7], count[7], v7, q7 = readfile("70 mm.txt")

steps = [0]*8
count = [0]*8
data1, steps[0], count[0] = readfile("10 mm.txt")
data2, steps[1], count[1] = readfile("20 mm.txt")
data3, steps[2], count[2] = readfile("30 mm.txt")
data4, steps[3], count[3] = readfile("40 mm.txt")
data5, steps[4], count[4] = readfile("50 mm.txt")
data6, steps[5], count[5] = readfile("60 mm.txt")
data7, steps[6], count[6] = readfile("70 mm.txt")
data8, steps[7], count[7] = readfile("80 mm.txt")

data1 = np.sqrt(2 * (data1 - 840) / 1.225)
data2 = np.sqrt(2 * (data2 - 840) / 1.225)
data3 = np.sqrt(2 * (data3 - 840) / 1.225)
data4 = np.sqrt(2 * (data4 - 840) / 1.225)
data5 = np.sqrt(2 * (data5 - 840) / 1.225)
data6 = np.sqrt(2 * (data6 - 840) / 1.225)
data7 = np.sqrt(2 * (data7 - 840) / 1.225)
data8 = np.sqrt(2 * (data8 - 840) / 1.225)




x = np.linspace(-85, 30, 190)
 
fig, ax = plt.subplots(figsize=(16,10), dpi=400)
ax.plot(x, data1, linewidth = 1, color = 'r', label = 'D = 10 mm')
ax.plot(x, data2, linewidth = 1, color ='b', label = 'D = 20 mm')
ax.plot(x, data3, linewidth = 1, color = 'brown', label = 'D = 30 mm')
ax.plot(x, data4, linewidth = 1, color = 'lime', label = 'D = 40 mm')
ax.plot(x, data5, linewidth = 1, color = 'navy', label = 'D = 50 mm')
ax.plot(x, data6, linewidth = 1, color  = 'cyan', label = 'D = 60 mm')
ax.plot(x, data7, linewidth = 1, color = 'darkmagenta', label = 'D = 70 mm')
ax.plot(x, data8, linewidth = 1, color = 'black', label = 'D = 80 mm')

ax.legend() 
 
plt.title("Скорость потока воздуха в сечении затопленной струи", fontstyle = 'italic', horizontalalignment = 'center')
plt.xlabel("Положение трубки Пито относительно центра струи [мм]")
plt.ylabel("Скорость воздуха [м/с]")
 
 
plt.grid(which='major', color='green', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', color='green', linestyle='--', linewidth = 0.25)

plt.xlim([-30, 30])
 
plt.minorticks_on()
 
fig.savefig("velocity-outgo.png")
 
 
#plt.show()