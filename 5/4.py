import json
import csv
import sys
import os


def json_to_csv(json_file):
    # Открываем и читаем JSON файл
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Получаем имя корневого ключа
    root_key = list(data.keys())[0]

    # Данные для записи в CSV
    rows = data[root_key]

    # Определяем имя результирующего CSV файла
    csv_file = os.path.join(os.path.dirname(json_file), f"{root_key}.csv")

    # Определяем заголовки (ключи словаря)
    headers = rows[0].keys()

    # Записываем данные в CSV файл
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"CSV файл '{csv_file}' успешно создан.")


json_file = sys.argv[1]
json_to_csv(json_file)
