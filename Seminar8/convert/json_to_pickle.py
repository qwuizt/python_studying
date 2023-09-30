import os
import json
import pickle


def convert_json_to_pickle(directory):
    if not os.path.exists(directory):
        print(f"Директория {directory} не существует.")
        return

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_file_path = os.path.join(directory, filename)
            pickle_file_path = os.path.splitext(json_file_path)[0] + ".pickle"

            with open(json_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)

            with open(pickle_file_path, "wb") as pickle_file:
                pickle.dump(data, pickle_file)

            print(f"Файл {json_file_path} успешно конвертирован в {pickle_file_path}.")


directory_path = ""  # path to DIRECTORY!
convert_json_to_pickle(directory_path)
