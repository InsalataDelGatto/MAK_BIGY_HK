import random as rd
import numpy as np
import matplotlib.pyplot as plt

attempts = 5_000_000
resolution = 1_000_000_000_000

def try_point():
    a = rd.randint(0,2 * resolution)
    b = rd.randint(0,2 * resolution)
    if (a-(1*resolution))**2 + b**2 <= (1*resolution)**2 and a**2 + (b-(1*resolution))**2 <= (1*resolution)**2:
        return False

    if (a-(1*resolution))**2 + b**2 <= (1*resolution)**2 or a**2 + (b-(1*resolution))**2 <= (1*resolution)**2:
        return True
    
    return False

def draw_point():
    a = rd.randint(0,2 * resolution)
    b = rd.randint(0,2 * resolution)
    if (a-(1*resolution))**2 + b**2 <= (1*resolution)**2 and a**2 + (b-(1*resolution))**2 <= (1*resolution)**2:
        l.append(a)
        m.append(b)
    elif (a-(1*resolution))**2 + b**2 <= (1*resolution)**2 or a**2 + (b-(1*resolution))**2 <= (1*resolution)**2:
        x.append(a)
        y.append(b)
    else:
        l.append(a)
        m.append(b)

x = []
y = []
l = []
m = []

for i in range(attempts):
    draw_point()

fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect('equal')

plt.scatter(x,y)
plt.scatter(l,m)
plt.show()

successes = 0
for i in range(attempts):
    if not try_point():
        successes += 1

print(16*(1-(successes/attempts)))
