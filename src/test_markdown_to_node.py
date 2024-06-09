import unittest
from textnode import TextNode
from inline_markdown import split_nodes_delimiter

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is a text node `with a code block in it` and I am splitting it.", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            new_nodes,
              [
                  TextNode("This is a text node ", "text"),
                  TextNode("with a code block in it", "code"),
                  TextNode(" and I am splitting it.", "text")
              ]
        )

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is a text node **with bold words in it** and I am splitting it.", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            new_nodes,
              [
                  TextNode("This is a text node ", "text"),
                  TextNode("with bold words in it", "bold"),
                  TextNode(" and I am splitting it.", "text")
              ]
        )

    def test_split_nodes_delimiter_starting_italic(self):
        node = TextNode("*This is a line of italic* at the beginning.", "text")
        new_nodes = split_nodes_delimiter([node], "*", "code")
        self.assertListEqual(
            new_nodes,
              [
                  TextNode("This is a line of italic", "italic"),
                  TextNode(" at the beginning.", "text"),
              ]
        )

    def test_split_nodes_delimiter_multiple_italic(self):
        node = TextNode("*This is a line of italic* at the beginning. *Also at the end.*", "text")
        new_nodes = split_nodes_delimiter([node], "*", "code")
        self.assertListEqual(
            new_nodes,
              [
                  TextNode("This is a line of italic", "italic"),
                  TextNode(" at the beginning. ", "text"),
                  TextNode("Also at the end.", "italic"),
              ]
        ) 
