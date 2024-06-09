def count_unique_numbers(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)


input_numbers = input("Введите список чисел, разделенных запятой: ")
numbers_list = [int(num) for num in input_numbers.split(',')]
unique_count = count_unique_numbers(numbers_list)
print("Количество различных чисел:", unique_count)
