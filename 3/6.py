def create_acronym(phrase):
    words = phrase.split()
    acronym = ""
    for word in words:
        if word:
            acronym += word[0].upper()
    return acronym


input_phrase = input("Введите строку: ")
acronym = create_acronym(input_phrase)
print("Аббревиатура:", acronym)
