import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(X**2 + Y**2)  # MSE
# Z2 = np.log(Z)
# Построение первого трехмерного графика
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('Среднеквадратичное отклонение')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Построение второго трехмерного графика с логарифмическим масштабом по Я
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
# ax2.plot_surface(X, Y, Z2, cmap='viridis')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_title('Среднеквадратичное отклонение (логарифмическая ось Z)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_zscale('log')

plt.show()
