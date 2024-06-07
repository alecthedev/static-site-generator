import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node  = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is another test", "italic", "https://google.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node2, node3)

    def test_repr(self):
        node = TextNode("This is a text node without url", "italic")
        node2 = TextNode("This is a text node with url", "italic", "https://google.com")
        node_expected_string  = "TextNode(This is a text node without url, italic, None)"
        node2_expected_string = "TextNode(This is a text node with url, italic, https://google.com)"
        self.assertEqual(str(node), node_expected_string)
        self.assertEqual(str(node2), node2_expected_string)

if __name__ == "__main__":
    unittest.main()
