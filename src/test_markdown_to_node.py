import unittest

from markdown_to_node import *
from textnode import TextNode


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode(
            "This is a text node `with a code block in it` and I am splitting it.",
            "text",
        )
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a text node ", "text"),
                TextNode("with a code block in it", "code"),
                TextNode(" and I am splitting it.", "text"),
            ],
        )

    def test_split_nodes_delimiter_bold(self):
        node = TextNode(
            "This is a text node **with bold words in it** and I am splitting it.",
            "text",
        )
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a text node ", "text"),
                TextNode("with bold words in it", "bold"),
                TextNode(" and I am splitting it.", "text"),
            ],
        )

    def test_split_nodes_delimiter_starting_italic(self):
        node = TextNode("*This is a line of italic* at the beginning.", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a line of italic", "italic"),
                TextNode(" at the beginning.", "text"),
            ],
        )

    def test_split_nodes_delimiter_multiple_italic(self):
        node = TextNode(
            "*This is a line of italic* at the beginning. *Also at the end.*", "text"
        )
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is a line of italic", "italic"),
                TextNode(" at the beginning. ", "text"),
                TextNode("Also at the end.", "italic"),
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
            "text",
        )

        self.assertListEqual(
            split_nodes_image([image_node]),
            [
                TextNode("This is text with an ", "text"),
                TextNode(
                    "image",
                    "image",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and another ", "text"),
                TextNode(
                    "second image",
                    "image",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
            ],
        )

    def test_split_nodes_link(self):
        link_node = TextNode(
            "This is text with a [link](https://www.google.com) and another [second link](https://www.bing.com)",
            "text",
        )

        self.assertListEqual(
            split_nodes_link([link_node]),
            [
                TextNode("This is text with a ", "text"),
                TextNode("link", "link", "https://www.google.com"),
                TextNode(" and another ", "text"),
                TextNode("second link", "link", "https://www.bing.com"),
            ],
        )
