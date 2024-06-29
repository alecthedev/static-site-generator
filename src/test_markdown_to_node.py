import unittest

from markdown_to_node import *
from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode(
            "This is a text node `with a code block in it` and I am splitting it.",
            text_type_text,
        )
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a text node ", text_type_text),
                TextNode("with a code block in it", text_type_code),
                TextNode(" and I am splitting it.", text_type_text),
            ],
        )

    def test_split_nodes_delimiter_bold(self):
        node = TextNode(
            "This is a text node **with bold words in it** and I am splitting it.",
            text_type_text,
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a text node ", text_type_text),
                TextNode("with bold words in it", text_type_bold),
                TextNode(" and I am splitting it.", text_type_text),
            ],
        )

    def test_split_nodes_delimiter_starting_italic(self):
        node = TextNode("*This is a line of italic* at the beginning.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a line of italic", text_type_italic),
                TextNode(" at the beginning.", text_type_text),
            ],
        )

    def test_split_nodes_delimiter_multiple_italic(self):
        node = TextNode(
            "*This is a line of italic* at the beginning. *Also at the end.*",
            text_type_text,
        )
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a line of italic", text_type_italic),
                TextNode(" at the beginning. ", text_type_text),
                TextNode("Also at the end.", text_type_italic),
            ],
        )

    def test_extract_markdown_images(self):
        images = extract_markdown_images(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://www.example.com/another)"
        )
        self.assertListEqual(
            images,
            [
                (
                    "image",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                ("another", "https://www.example.com/another"),
            ],
        )

    def test_extract_markdown_link(self):
        links = extract_markdown_links(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        )
        self.assertListEqual(
            links,
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another"),
            ],
        )

    def test_split_nodes_image(self):
        image_node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )

        self.assertListEqual(
            split_nodes_image([image_node]),
            [
                TextNode("This is text with an ", text_type_text),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
            ],
        )

    def test_split_nodes_link(self):
        link_node = TextNode(
            "This is text with a [link](https://www.google.com) and another [second link](https://www.bing.com)",
            text_type_link,
        )

        self.assertListEqual(
            split_nodes_link([link_node]),
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://www.google.com"),
                TextNode(" and another ", text_type_text),
                TextNode("second link", text_type_link, "https://www.bing.com"),
            ],
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

        self.assertListEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
        )
