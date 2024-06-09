def count_words(text):
    words = text.split()
    word_counts = {}
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

def custom_sort(item):
    return (-item[1], item[0])


input_text = input("Введите текст: ")
word_counts = count_words(input_text)

sorted_words = sorted(word_counts.items(), key=custom_sort)

for word, count in sorted_words:
    print(word)
