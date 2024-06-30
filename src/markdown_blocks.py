from htmlnode import ParentNode
from markdown_to_node import text_to_textnodes
from textnode import text_node_to_html_node

block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"
block_type_paragraph = "paragraph"


def markdown_to_blocks(markdown):
    return markdown.strip().split("\n\n")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    node_list = []

    for block in blocks:
        node_list.append(block_to_html_node(block))

    return ParentNode("div", node_list)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_heading:
        return heading_block_to_html(block)
    if block_type == block_type_code:
        return code_block_to_html(block)
    if block_type == block_type_quote:
        return quote_block_to_html(block)
    if block_type == block_type_unordered_list:
        return unordered_list_block_to_html(block)
    if block_type == block_type_ordered_list:
        return ordered_list_block_to_html(block)
    if block_type == block_type_paragraph:
        return paragraph_block_to_html(block)
    raise ValueError("Block type invalid")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading

    if block.startswith("```") and block.endswith("```"):
        return block_type_code

    if any(line.startswith(">") for line in lines):
        return block_type_quote

    if any(line.startswith("* ") for line in lines) or any(
        line.startswith("- ") for line in lines
    ):
        return block_type_unordered_list

    if block.startswith("1. "):
        line_num = 1
        for line in lines:
            if not line.startswith(f"{line_num}. "):
                break
            line_num += 1
        return block_type_ordered_list

    return block_type_paragraph


def heading_block_to_html(block):
    heading_num = 0
    for c in block:
        if c == "#":
            heading_num += 1
        else:
            break

    return ParentNode(f"h{heading_num}", text_to_children(block.strip("# ")))


def code_block_to_html(block):
    return ParentNode("pre", [ParentNode("code", text_to_children(block.strip("` ")))])


def quote_block_to_html(block):
    quote_lines = []
    for line in block.split("\n"):
        quote_lines.append(line.strip("> "))
    children = text_to_children(" ".join(quote_lines))

    return ParentNode("blockquote", children)


def unordered_list_block_to_html(block):
    list_items = block.split("\n")
    node_list = []
    for item in list_items:
        node_list.append(ParentNode("li", text_to_children(item.strip("*- "))))
    return ParentNode("ul", node_list)


def ordered_list_block_to_html(block):
    list_items = block.split("\n")
    node_list = []
    for item in list_items:
        node_list.append(ParentNode("li", text_to_children(item[3:])))
    return ParentNode("ol", node_list)


def paragraph_block_to_html(block):
    return ParentNode("p", text_to_children(" ".join(block.split("\n"))))
