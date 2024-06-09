import numpy as np


x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

zero_indices = np.where(x == 0)[0]
valid_indices = zero_indices[zero_indices + 1 < len(x)]
candidates = x[valid_indices + 1]
if len(candidates) > 0:
    max_element = np.max(candidates)
    print(
        f"Максимальный элемент среди элементов, перед которыми стоит нулевой: {max_element}"
    )
else:
    print("Нет элементов, следующих за нулями")
