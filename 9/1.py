import numpy as np

matrix = np.array([[3, 4, 17, -3],
                   [5, 11, -1, 6],
                   [0, 2, -5, 8]])

np.savetxt('9/matrix.txt', matrix, fmt='%d')

loaded_matrix = np.loadtxt('9/matrix.txt', dtype=int)


sum_elements = np.sum(loaded_matrix)
max_element = np.max(loaded_matrix)
min_element = np.min(loaded_matrix)

print(f"Сумма {sum_elements}, Макс элемент {max_element}, Мин элемент {min_element}")
