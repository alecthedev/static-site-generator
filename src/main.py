import os
import shutil

from markdown_to_html import generate_page
from static_to_public import copy_dir


def main():
    static_path = "./static"
    public_path = "./public/"

    index_md_path = "./content/index.md"
    template_path = "./template.html"
    index_html_path = "./public/index.html"

    if os.path.exists(public_path):
        print(f"Removing {public_path}")
        shutil.rmtree(public_path)

    print(f"Copying {static_path} to {public_path}")
    copy_dir(static_path, public_path)

    generate_page(index_md_path, template_path, index_html_path)


main()
