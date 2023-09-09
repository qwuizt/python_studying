import os


def split_file_path(path_to_file):
    directory, full_file_name = os.path.split(path_to_file)
    file_name, file_extension = os.path.splitext(full_file_name)
    return (directory, file_name, file_extension)


file_path = "Seminar5/example.txt"  # copy file path
result = split_file_path(file_path)
print(result)
