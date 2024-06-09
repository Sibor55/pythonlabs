import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# столбец species
species_column = iris[:, 4]

# уникальные значения и их количество
unique_values, counts = np.unique(species_column, return_counts=True)


for value, count in zip(unique_values, counts):
    print("Уникальное значение:", value.decode('utf-8'), ", Количество:", count)
