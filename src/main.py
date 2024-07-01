import os
import shutil

from markdown_to_html import generate_all_pages
from static_to_public import copy_dir


def main():
    static_path = "./static"
    public_path = "./public"
    content_path = "./content"
    template_path = "./template.html"

    if os.path.exists(public_path):
        print(f"Removing {public_path}")
        shutil.rmtree(public_path)

    print(f"Copying {static_path} to {public_path}")
    copy_dir(static_path, public_path)

    generate_all_pages(content_path, template_path, public_path)


main()
