def check_city(city, cities):
    if city in cities:
        return "REPEAT"
    else:
        cities.add(city)
        return "OK"



n = int(input("Введите количество названных городов: "))
cities_set = set()

for _ in range(n):
    city = input("Введите название города: ")
    result = check_city(city, cities_set)
    print(result)
