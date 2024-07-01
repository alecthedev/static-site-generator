import os
import shutil


def copy_dir(source_path, dest_path):
    # recursively copies source directory to destination directory

    if not os.path.exists(source_path):
        raise FileNotFoundError("Source path not found")

    os.mkdir(dest_path)

    for file_name in os.listdir(source_path):
        file_source_path = os.path.join(source_path, file_name)
        file_dest_path = os.path.join(dest_path, file_name)

        if os.path.isfile(file_source_path):
            print(f"Copying {file_source_path} to {file_dest_path}")
            shutil.copy(file_source_path, file_dest_path)
        else:
            print(f"Copying {file_source_path} to {file_dest_path}")
            copy_dir(file_source_path, file_dest_path)
