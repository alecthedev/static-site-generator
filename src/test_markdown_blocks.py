import unittest

from markdown_blocks import *


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """This is a **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        self.assertListEqual(
            markdown_to_blocks(markdown),
            [
                "This is a **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
