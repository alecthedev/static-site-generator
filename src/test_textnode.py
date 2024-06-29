import unittest

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        node3 = TextNode("This is another test", text_type_italic, "https://google.com")
        self.assertEqual(str(node), str(node2))
        self.assertNotEqual(str(node2), str(node3))

    def test_repr(self):
        node = TextNode("This is a text node without url", text_type_italic)
        node2 = TextNode(
            "This is a text node with url", text_type_italic, "https://google.com"
        )
        node_expected_string = "TextNode(This is a text node without url, italic, None)"
        node2_expected_string = (
            "TextNode(This is a text node with url, italic, https://google.com)"
        )
        self.assertEqual(str(node), node_expected_string)
        self.assertEqual(str(node2), node2_expected_string)


if __name__ == "__main__":
    unittest.main()
