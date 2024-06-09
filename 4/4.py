def count_previous_occurrences(text):
    words = text.split()
    occurrences = {}
    counts = []

    for word in words:
        counts.append(occurrences.get(word, 0))
        occurrences[word] = occurrences.get(word, 0) + 1

    return counts


input_text = input("Введите строку текста: ")
results = count_previous_occurrences(input_text)

print(" ".join(map(str, results)))
