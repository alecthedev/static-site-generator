import os
import shutil

from static_to_public import copy_dir


def main():
    static_path = "./static"
    public_path = "./public/"

    if os.path.exists(public_path):
        print(f"Removing {public_path}")
        shutil.rmtree(public_path)

    print(f"Copying {static_path} to {public_path}")
    copy_dir(static_path, public_path)


main()
