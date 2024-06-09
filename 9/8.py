import numpy as np

arr = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])

# индексы ненулевых элементов
nonzero_indices = np.nonzero(arr)

print("Индексы ненулевых элементов:", nonzero_indices)
