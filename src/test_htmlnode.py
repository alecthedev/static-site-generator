import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode("p", "This is a paragraph HTMLNode.", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertEqual(node2.props_to_html(),"")

    def test_repr(self):
        node1 = HTMLNode("p", "This is a paragraph HTMLNode.", None, {"href": "https://www.google.com", "target": "_blank"})
        node3 = HTMLNode("h1", "Hello", [node1], None)
        self.assertEqual(str(node3), "HTMLNode(Tag: h1, Value: Hello, Children: 1, Properties: 0)")
        self.assertEqual(str(node1), 'HTMLNode(Tag: p, Value: This is a paragraph HTMLNode., Children: 0, Properties: 2)')

if __name__ == "__main__":
    unittest.main()
