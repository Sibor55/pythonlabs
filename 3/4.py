def count_string_repeats(strings):
    counts = {}
    for string in strings:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1
    return counts


input_strings = input("Введите список строк, разделенных пробелом: ").split()
repeats = count_string_repeats(input_strings)
for string, count in repeats.items():
    print(count, end=" ")
