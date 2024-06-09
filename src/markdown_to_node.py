import re

from textnode import TextNode

def split_nodes_delimiter(original_nodes, delimiter, text_type):
    output_nodes = []
    
    for node in original_nodes:
        if not isinstance(node, TextNode):
            output_nodes.append(original_nodes)
            continue
        split_nodes = []
        split_texts = node.text.split(delimiter)
        if len(split_texts) % 2 == 0:
            raise ValueError(f"Invalid syntax, Markdown tag not closed: '{delimiter}'.")
        for i in range(len(split_texts)):
            if split_texts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_texts[i], "text"))
            else:
                split_nodes.append(TextNode(split_texts[i], text_type))
        output_nodes.extend(split_nodes)
    return output_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
