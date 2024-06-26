import os
from pathlib import Path

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.lstrip("# ")
    raise ValueError("File must contain a title (h1)")


def generate_page(source_path, template_path, dest_path):

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source path not found: {source_path}")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template path not found: {template_path}")

    print(f"Generating a page from {source_path} to {dest_path}")
    print(f"Using template: {template_path}")

    md_file = open(source_path, "r")
    md_content = md_file.read()
    md_file.close()

    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()

    title = extract_title(md_content)
    html = markdown_to_html_node(md_content).to_html()

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    target_file = open(dest_path, "w")
    target_file.write(template_content)
    target_file.close()


def generate_all_pages(source_dir_path, template_path, dest_dir_path):
    # recursively generates all .md from source to destination using defined template
    for filename in os.listdir(source_dir_path):
        file_source_path = os.path.join(source_dir_path, filename)
        file_dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(file_source_path):
            file_dest_path = Path(file_dest_path).with_suffix(".html")
            generate_page(file_source_path, template_path, file_dest_path)
        else:
            generate_all_pages(file_source_path, template_path, file_dest_path)
