import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre


fig, ax = plt.subplots()

# Задание заголовка
plt.title("Полиномы Лежандра")

# диапазон значений x
x = np.linspace(-1, 1, 1000)


for n in range(1, 8):
    y = legendre(n)(x)
    ax.plot(x, y, label=f'n = {n}')

# Добавление легенду графика
ax.legend()

# Отображение графика
plt.show()
