def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


def print_pascals_triangle(triangle):
    n = len(triangle)
    max_length = len(' '.join(map(str, triangle[-1])))  # ширина последнего ряда
    for row in triangle:
        row_str = ' '.join(map(str, row))
        spaces = ' ' * ((max_length - len(row_str)) // 2)  # чтобы был по центру
        print(spaces + row_str)


n = int(input("Введите количество строк треугольника Паскаля: "))
pascals_triangle = generate_pascals_triangle(n)
print_pascals_triangle(pascals_triangle)
