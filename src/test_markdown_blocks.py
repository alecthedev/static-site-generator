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

    def test_block_to_block_type_heading(self):
        heading = "### This is a heading"
        self.assertEqual(block_to_block_type(heading), block_type_heading)

    def test_block_to_block_type_code(self):
        code = "```\ndef code_block():\n\tprint('this is code')```"
        self.assertEqual(block_to_block_type(code), block_type_code)

    def test_block_to_block_type_quote(self):
        quote = "> Make it a great day, or not.\n> The choice is yours."
        self.assertEqual(block_to_block_type(quote), block_type_quote)

    def test_block_to_block_type_unordered_list_dash(self):
        ul = "- This is an unordered list\n- using dashes"
        self.assertEqual(block_to_block_type(ul), block_type_unordered_list)

    def test_block_to_block_type_unordered_list_ast(self):
        ul = "* Also is an unordered list\n* using asterix"
        self.assertEqual(block_to_block_type(ul), block_type_unordered_list)

    def test_block_to_block_type_ordered_list(self):
        ol = "1. first item\n2. second item\n3. third item"
        self.assertEqual(block_to_block_type(ol), block_type_ordered_list)

    def test_block_to_block_type_paragraph(self):
        p = "Just a normal paragraph\nNothing to be concerned about."
        self.assertEqual(block_to_block_type(p), block_type_paragraph)
