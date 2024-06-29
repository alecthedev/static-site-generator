from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)


def main():
    dummy_node = TextNode("This is a text node", text_type_link, "https://www.boot.dev")
    print(dummy_node)


main()
