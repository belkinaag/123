import numpy as np
import matplotlib.pyplot as plt
with open("New.txt", "r") as new:
    tmp = [float(i) for i in new.read().split("\n")]
    print(tmp)

dats_array = np.loadtxt("data.txt", dtype=int)

dats_array = 3.3 / 256 * dats_array

fig, ax = plt.subplots(figsize=(16,10), dpi =400)
ax.plot(dats_array, label = 'линия интерполяции', markevery = 125, marker = '.', markersize = 15)
ax.set_xlabel('t, c')
ax.set_ylabel('U(t), у.е')
ax.set_title("Зависимость напряжения на конденсаторе от времени")
ax.legend()

plt.text(1000, 1.25, "Время зарядки 28 с; разрядки - 32 с", fontsize=15)



ax.minorticks_on()


ax.grid(which='major',
        color = 'k', 
        linewidth = 2)

ax.grid(which='minor', 
        color = 'k', 
        linestyle = ':')




fig.savefig("1.png")
plt.show()