def decompress_string(s):
    decompressed = []
    i = 0
    while i < len(s):
        char = s[i]
        count = 1  # если нет числа после буквы
        # цикл для проверки цифр числа
        j = i + 1
        while j < len(s) and s[j].isdigit():
            j += 1
        if j > i + 1:
            count = int(s[i + 1 : j])
        decompressed.append(char * count)
        i = j
    return "".join(decompressed)


input_string = input("Введите закодированную строку: ")
result = decompress_string(input_string)
print("Исходная строка:", result)
