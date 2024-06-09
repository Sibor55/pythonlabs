import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def lissajous(a, b, delta):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = np.sin(a * t)
    y = np.sin(b * t + delta)
    return x, y


def update(frame):
    ax.clear()
    a = frame
    b = 1
    x, y = lissajous(a, b, 0)
    ax.plot(x, y)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title(f'{a}:1')


fig, ax = plt.subplots()


ani = FuncAnimation(fig, update, frames=np.linspace(0.1, 1, 100), interval=50)
# ani = FuncAnimation(fig, update, frames=np.linspace(1, 10, 100), interval=50)

plt.show()
