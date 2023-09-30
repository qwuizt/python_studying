import json
import csv
import pickle


def save_to_json(data, output_path):
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def save_to_csv(data, output_path):
    with open(output_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


def save_to_pickle(data, output_path):
    with open(output_path, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
