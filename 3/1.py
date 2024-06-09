def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed.append(s[i - 1] + str(count))
            else:
                compressed.append(s[i - 1])
            count = 1
    # Добавляем последний символ и его количество
    if count > 1:
        compressed.append(s[-1] + str(count))
    else:
        compressed.append(s[-1])
    return "".join(compressed)


input_string = input("Введите строку символов: ")
result = compress_string(input_string)
print("Закодированная строка:", result)
