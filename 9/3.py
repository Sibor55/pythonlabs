import numpy as np


np.random.seed(0)
array = np.random.randn(10, 4)


min_value = np.min(array)
print(f"Минимальное значение: {min_value}")

max_value = np.max(array)
print(f"Максимальное значение: {max_value}")

mean_value = np.mean(array)
print(f"Среднее значение: {mean_value}")

std_deviation = np.std(array)
print(f"Стандартное отклонение: {std_deviation}")

first_5_rows = array[:5]
print("Первые 5 строк массива:")
print(first_5_rows)
