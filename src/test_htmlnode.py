import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph HTMLNode.", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(),"")

    def test_repr(self):
        node1 = HTMLNode("p", "This is a paragraph HTMLNode.", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("h1", "Hello", [node1], None)
        self.assertEqual(str(node1), 'HTMLNode(Tag: p, Value: This is a paragraph HTMLNode., Children: 0, Properties: 2)')
        self.assertEqual(str(node2), "HTMLNode(Tag: h1, Value: Hello, Children: 1, Properties: 0)")

    def test_leaf_to_html(self):
        node = LeafNode("a", "Click Here!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Here!</a>')

    def test_leaf_to_html_no_props(self):
        node = LeafNode("h1", "Heading1", None)
        self.assertEqual(node.to_html(), "<h1>Heading1</h1>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "raw text")
        self.assertEqual(node.to_html(), "raw text")

if __name__ == "__main__":
    unittest.main()
