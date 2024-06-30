import unittest

from markdown_blocks import *
from textnode import TextNode, text_type_text


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

    # -------------------------- block_type tests ------------------------------

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

    # -------------------------- MD to HTML tests ------------------------------

    def test_heading_to_html(self):
        markdown = "## Level 2 heading"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, "<div><h2>Level 2 heading</h2></div>")

    def test_heading_with_paragraph_to_html(self):
        markdown = """
## Level 2 heading

Here is some paragraph text

#### A level 4 heading

and some more paragraph text
that is on more than one line in the markdown

"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Level 2 heading</h2><p>Here is some paragraph text</p><h4>A level 4 heading</h4><p>and some more paragraph text that is on more than one line in the markdown</p></div>",
        )

    def test_code_block_to_html(self):
        markdown = """
```
def code():
    this_is = "code"
```
"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><pre><code>\ndef code():\n    this_is = "code"\n</code></pre></div>',
        )

    def test_quote_to_html(self):
        markdown = """
What follows is a blockquote:

> Make it a great day, or not, 
> the choice is yours.
"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>What follows is a blockquote:</p><blockquote>Make it a great day, or not, the choice is yours.</blockquote></div>",
        )

    def test_lists_to_html(self):
        markdown = """
- unordered list first item
- and the second item

1. ordered list 1
2. ordered list 2
3. ordered list 3
"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>unordered list first item</li><li>and the second item</li></ul><ol><li>ordered list 1</li><li>ordered list 2</li><li>ordered list 3</li></ol></div>",
        )
