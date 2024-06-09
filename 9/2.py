import numpy as np


def run_length_encoding(x):
    if len(x) == 0:
        return (np.array([]), np.array([]))

    # список для хранения уникальных значений и их количества
    values = []
    counts = []

    # первое значение и счетчик
    current_value = x[0]
    count = 1

    # Проходим по массиву, начиная со второго элемента
    for i in range(1, len(x)):
        if x[i] == current_value:
            count += 1
        else:
            values.append(current_value)
            counts.append(count)
            current_value = x[i]
            count = 1

    # Не забываем добавить последний элемент и его счетчик
    values.append(current_value)
    counts.append(count)

    return (np.array(values), np.array(counts))


x = np.array([2, 2, 2, 3, 3, 3, 5])
result = run_length_encoding(x)
print(result)
