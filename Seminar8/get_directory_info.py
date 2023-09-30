import os
from file_savers import save_to_pickle, save_to_json, save_to_csv


def get_directory_size(dir_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def process_directory(dir_path):
    dir_info = {
        "type": "directory",
        "size": get_directory_size(dir_path),
        "contents": []
    }

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            item_info = {
                "type": "file",
                "size": os.path.getsize(item_path)
            }
        elif os.path.isdir(item_path):
            item_info = process_directory(item_path)
        else:
            continue

        item_info["name"] = item
        dir_info["contents"].append(item_info)

        save_to_csv(dir_info, "info.csv")
        save_to_json(dir_info, "info.json")
        save_to_pickle(dir_info, "info.pickle")
    return dir_info


if __name__ == "__main__":
    path_directory = ""  # Path to directory
    process_directory(path_directory)





