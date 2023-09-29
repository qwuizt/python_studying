import os


def batch_rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range):
    files = os.listdir(directory)
    files = [file for file in files if file.endswith(source_extension)]
    files.sort()
    counter = 1
    for file in files:
        original_name = file[name_range[0] - 1:name_range[1]]
        new_name = f"{original_name}_{desired_name}_{counter:0{num_digits}d}.{target_extension}"
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        counter += 1


directory = "file directory path"
desired_name = "test"
num_digits = 1  # number of digits in the file at the end
source_extension = ".txt"
target_extension = ".md"
name_range = [3, 6]

batch_rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range)
