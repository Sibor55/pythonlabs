# Сохранение текста в файл
matrix_text = """3,4,17,-3
5,11,-1,6
0,2,-5,8"""

file_path = '9/matrix.txt'

with open(file_path, 'w') as file:
    file.write(matrix_text)

matrix = []

with open(file_path, 'r') as file:
    for line in file:
        row = [int(num) for num in line.strip().split(',')]
        matrix.append(row)

# Нахождение суммы, максимального и минимального элементов
total_sum = 0
max_element = float('-inf')
min_element = float('inf')

for row in matrix:
    for num in row:
        total_sum += num
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num

print(f"Сумма всех элементов матрицы: {total_sum}")
print(f"Максимальный элемент матрицы: {max_element}")
print(f"Минимальный элемент матрицы: {min_element}")
