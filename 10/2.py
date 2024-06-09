import numpy as np
import matplotlib.pyplot as plt


# Функция для построения фигуры Лиссажу
def lissajous(a, b, delta):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y


# Создание фигуры и осей
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Соотношения частот для каждого графика
frequencies = [(3, 2), (3, 4), (5, 4), (5, 6)]

# Построение фигур Лиссажу для каждого соотношения частот
for i, (a, b) in enumerate(frequencies):
    row = i // 2
    col = i % 2
    x, y = lissajous(a, b, np.pi / 2)
    axs[row, col].plot(x, y)
    axs[row, col].set_title(f"{a}:{b}")
    axs[row, col].set_aspect("equal")

# Отображение графиков
plt.show()
