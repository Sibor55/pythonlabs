mat = [[2, 3, -1], [-4, 0, 2], [-2, 4, 1]]


def lin_zav(mtx):
    cols = []
    for i in range(len(mtx[0])):
        col = []
        for row in mtx:
            col.append(row[i])
        cols.append(col)

    # Проверяем линейную зависимость столбцов
    for i in range(len(cols)):
        for j in range(len(cols) - 1):
            if cols[i][i] == 0:  # Проверяем, если элемент на главной диагонали равен 0
                return True  # Возвращаем True, так как столбцы линейно зависимы из-за нулевого элемента на диагонали
            scalar = (
                cols[j][i] / cols[i][i]
            )  # Вычисляем коэффициент для приведения элементов столбцов к линейной комбинации
            is_lin_comb = True  # Флаг для проверки линейной комбинации

            for k in range(len(cols)):
                if cols[j][k] != cols[j][i] * scalar + cols[i][k]:
                    is_lin_comb = False
                    break
            if is_lin_comb:
                return True
    return False


print(lin_zav(mat))


# Из курса алгебры мы узнали, что если определитель матрицы 3 на 3 = 0, то вектора линейно зависимы
# Просто считаем определитель и проверяем равен ли 0, это второй способ.
def check_3by3_det(mtx):
    return 0 == (
        (
            mtx[0][0] * mtx[1][1] * mtx[2][2]
            + mtx[0][1] * mtx[1][2] * mtx[2][0]
            + mtx[0][2] * mtx[1][0] * mtx[2][1]
            - mtx[0][2] * mtx[1][1] * mtx[2][0]
            - mtx[0][1] * mtx[1][0] * mtx[2][2]
            - mtx[0][0] * mtx[1][2] * mtx[2][1]
        )
    )


print(check_3by3_det(mat))
