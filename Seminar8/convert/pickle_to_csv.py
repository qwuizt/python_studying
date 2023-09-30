import os
import csv
import pickle


def convert_pickle_to_csv(directory, index_dict):
    if not os.path.exists(directory):
        print(f"Директория {directory} не существует.")
        return

    for filename in os.listdir(directory):
        if filename.endswith(".pickle"):
            pickle_file_path = os.path.join(directory, filename)
            csv_file_path = os.path.splitext(pickle_file_path)[0] + ".csv"

            with open(pickle_file_path, "rb") as pickle_file:
                data = pickle.load(pickle_file)

            if index_dict < 0 or index_dict >= len(data):
                print("Индекс словаря для заголовков недопустим.")
                return
            fieldnames = data[index_dict].keys()

            with open(csv_file_path, "w", newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

            print(f"Файл {pickle_file_path} успешно конвертирован в {csv_file_path}.")


directory_path = ""  # path to DIRECTORY!
index_dict = int(input("Введите индекс словаря: "))
convert_pickle_to_csv(directory_path, index_dict)




