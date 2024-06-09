def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


def convert_to_sierpinski(triangle):
    sierpinski_triangle = []
    for row in triangle:
        sierpinski_row = ['*' if num % 2 != 0 else ' ' for num in row]
        sierpinski_triangle.append(sierpinski_row)
    return sierpinski_triangle


def print_sierpinski(triangle):
    n = len(triangle)
    max_length = len(' '.join(triangle[-1]))    
    for row in triangle:
        row_str = ' '.join(row)
        spaces = ' ' * ((max_length - len(row_str)) // 2)  
        print(spaces + row_str + spaces)


n = int(input("Введите количество строк треугольника Серпинского(минимум 8 для трех итераций): "))
pascals_triangle = generate_pascals_triangle(n)
sierpinski_triangle = convert_to_sierpinski(pascals_triangle)
print_sierpinski(sierpinski_triangle)

