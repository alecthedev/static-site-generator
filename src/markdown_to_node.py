import re

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)


def split_nodes_delimiter(original_nodes, delimiter, text_type):
    output_nodes = []

    for node in original_nodes:
        if node.text_type != text_type_text:
            output_nodes.append(node)
            continue
        split_nodes = []
        split_texts = node.text.split(delimiter)
        if len(split_texts) % 2 == 0:
            raise ValueError(f"Invalid syntax, Markdown tag not closed: '{delimiter}'.")
        for i in range(len(split_texts)):
            if split_texts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_texts[i], text_type_text))
            else:
                split_nodes.append(TextNode(split_texts[i], text_type))
        output_nodes.extend(split_nodes)
    return output_nodes


def split_nodes_image(original_nodes):
    output_nodes = []

    for node in original_nodes:
        if not isinstance(node, TextNode):
            output_nodes.append(node)
            continue
        # extract images (as text, to create nodes), or simply append if none are found
        node_text = node.text
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            output_nodes.append(node)
            continue
        for image in images:
            # separate image text from image hyperlink
            split_image = node_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(split_image) != 2:
                raise ValueError("Invalid syntax, Markdown tag not closed: image")
            if split_image[0] != "":
                # if there is text in front of the link, make a new text node
                output_nodes.append(TextNode(split_image[0], text_type_text))
            # create new TextNode of type "image"
            # image[0] being the text in front, image[1] being the url
            output_nodes.append(TextNode(image[0], text_type_image, image[1]))
            # if there is any text after the image tag, create a 'text' TextNode
            node_text = split_image[1]
        if node_text != "":
            output_nodes.append(TextNode(node_text, text_type_text))
    return output_nodes


def split_nodes_link(original_nodes):
    output_nodes = []

    for node in original_nodes:
        if not isinstance(node, TextNode):
            output_nodes.append(node)
            continue
        # extract links (as text, to create nodes), or simply append if none are found
        node_text = node.text
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            output_nodes.append(node)
            continue
        # separate link text from link url
        for link in links:
            split_link = node_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(split_link) != 2:
                ValueError("Invalid syntax, Markdown tag not closed: link")
            if split_link[0] != "":
                output_nodes.append(TextNode(split_link[0], text_type_text))
            # create new TextNode of type "link"
            # link[0] being the text in front, link[1] being the url
            output_nodes.append(TextNode(link[0], text_type_link, link[1]))
            # if there is any text after the link tag, create a 'text' TextNode
            node_text = split_link[1]
        if node_text != "":
            output_nodes.append(TextNode(node_text, text_type_text))
    return output_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def text_to_textnodes(text):
    # create a Textnode from the argument text, add to output list
    output_nodes = [TextNode(text, text_type_text)]
    # split each node in the list into more nodes if necessary
    output_nodes = split_nodes_delimiter(output_nodes, "**", text_type_bold)
    output_nodes = split_nodes_delimiter(output_nodes, "*", text_type_italic)
    output_nodes = split_nodes_delimiter(output_nodes, "`", text_type_code)
    output_nodes = split_nodes_image(output_nodes)
    output_nodes = split_nodes_link(output_nodes)

    return output_nodes
