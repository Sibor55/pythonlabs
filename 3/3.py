def number_to_words(num):
    units = [
        "",
        "один",
        "два",
        "три",
        "четыре",
        "пять",
        "шесть",
        "семь",
        "восемь",
        "девять",
    ]
    teens = [
        "",
        "одиннадцать",
        "двенадцать",
        "тринадцать",
        "четырнадцать",
        "пятнадцать",
        "шестнадцать",
        "семнадцать",
        "восемнадцать",
        "девятнадцать",
    ]
    tens = [
        "",
        "десять",
        "двадцать",
        "тридцать",
        "сорок",
        "пятьдесят",
        "шестьдесят",
        "семьдесят",
        "восемьдесят",
        "девяносто",
    ]
    hundreds = [
        "",
        "сто",
        "двести",
        "триста",
        "четыреста",
        "пятьсот",
        "шестьсот",
        "семьсот",
        "восемьсот",
        "девятьсот",
    ]
    thousand = "тысяча"
    if num == 1000:
        return thousand
    words = []
    if num >= 100:
        words.append(hundreds[num // 100])
        num %= 100
    if 10 < num < 20:
        words.append(teens[num - 10])
        return " ".join(words)
    if num >= 20 or num == 10:
        words.append(tens[num // 10])
        num %= 10
    if num > 0 and num <= 9:
        words.append(units[num])
    return " ".join(words).strip()


num = int(input("Введите число в диапазоне от 1 до 1000: "))
if 1 <= num <= 1000:
    print(number_to_words(num))
else:
    print("Число вне диапазона.")
