import csv
import os
import random
import sys


class CSVProcessor:
    def __init__(self, filepath, separator=","):
        self.filepath = filepath
        self.separator = separator
        self.data = []
        self.headers = []
        self._load_csv()

    def _load_csv(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=self.separator)
            self.headers = next(reader)
            self.data = [row for row in reader]

    def show(self, output_type="top", num_rows=5):
        if num_rows <= 0:
            print("Количество строк должно быть положительным числом.")
            return

        if len(self.data) < num_rows:
            print(f"В таблице недостаточно строк, всего {len(self.data)} строк.")
            num_rows = len(self.data)

        if output_type == "top":
            rows_to_show = self.data[:num_rows]
        elif output_type == "bottom":
            rows_to_show = self.data[-num_rows:]
        elif output_type == "random":
            rows_to_show = random.sample(self.data, num_rows)
        else:
            print("Недопустимый тип вывода. Используйте 'top', 'bottom' или 'random'.")
            return

        print(self.separator.join(self.headers))
        for row in rows_to_show:
            print(self.separator.join(row))

    def info(self):
        num_rows = len(self.data)
        num_cols = len(self.headers)
        print(f"{num_rows}x{num_cols}")

        field_info = {header: {"count": 0, "type": None} for header in self.headers}
        for row in self.data:
            for i, value in enumerate(row):
                if value:
                    field_info[self.headers[i]]["count"] += 1
                    if field_info[self.headers[i]]["type"] is None:
                        if value.isdigit():
                            field_info[self.headers[i]]["type"] = "int"
                        else:
                            field_info[self.headers[i]]["type"] = "string"
                    elif (
                        field_info[self.headers[i]]["type"] == "int"
                        and not value.isdigit()
                    ):
                        field_info[self.headers[i]]["type"] = "string"

        for header, info in field_info.items():
            print(f"{header} {info['count']} {info['type']}")

    def del_nan(self):
        initial_len = len(self.data)
        self.data = [row for row in self.data if all(row)]
        removed_count = initial_len - len(self.data)
        print(f"Удалено строк с пустыми значениями: {removed_count}")

    def make_ds(self):
        if not self.data:
            print("Нет данных для разделения.")
            return

        random.shuffle(self.data)
        split_idx = int(0.7 * len(self.data))
        train_data = self.data[:split_idx]
        test_data = self.data[split_idx:]

        os.makedirs("Itog1/workdata/Learning", exist_ok=True)
        os.makedirs("Itog1/workdata/Testing", exist_ok=True)

        self._save_csv("Itog1/workdata/Learning/train.csv", train_data)
        self._save_csv("Itog1/workdata/Testing/test.csv", test_data)

    def _save_csv(self, filepath, data):
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=self.separator)
            writer.writerow(self.headers)
            writer.writerows(data)



csv_file = sys.argv[1]
processor = CSVProcessor(csv_file)


processor.show(output_type="top", num_rows=5)
processor.info()
processor.del_nan()
processor.make_ds()
