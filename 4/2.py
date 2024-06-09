def is_subset(set1, set2):
    for element in set1:
        if element not in set2:
            return False
    return True


input_set1 = input("Введите элементы первого множества, разделенные запятой и без пробелов: ")
input_set2 = input("Введите элементы второго множества, разделенные запятой и без пробелов: ")

set1 = set(input_set1.split(','))
set2 = set(input_set2.split(','))

result = is_subset(set1, set2)

print(result)
