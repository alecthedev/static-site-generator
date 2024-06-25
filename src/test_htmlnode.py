import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "p",
            "This is a paragraph HTMLNode.",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_repr(self):
        node_1 = HTMLNode(
            "p",
            "This is a paragraph HTMLNode.",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        node_2 = HTMLNode("h1", "Hello", [node_1], None)
        self.assertEqual(
            str(node_1),
            "HTMLNode(Tag: p, Value: This is a paragraph HTMLNode., Children: 0, Properties: 2)",
        )
        self.assertEqual(
            str(node_2), "HTMLNode(Tag: h1, Value: Hello, Children: 1, Properties: 0)"
        )

    def test_leaf_to_html(self):
        node = LeafNode("a", "Click Here!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click Here!</a>'
        )

    def test_leaf_to_html_no_props(self):
        node = LeafNode("h1", "Heading1", None)
        self.assertEqual(node.to_html(), "<h1>Heading1</h1>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "raw text")
        self.assertEqual(node.to_html(), "raw text")

    def test_parent_to_html_two_children(self):
        node = ParentNode(
            "p",
            [LeafNode("i", "italic text"), LeafNode(None, "normal text")],
        )
        self.assertEqual(node.to_html(), "<p><i>italic text</i>normal text</p>")

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "body",
            [
                LeafNode("h1", "Heading1"),
                ParentNode(
                    "p",
                    [
                        LeafNode("i", "Some text"),
                        LeafNode("a", "A link", {"href": "https://www.google.com"}),
                    ],
                ),
                LeafNode("h4", "Heading4"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<body><h1>Heading1</h1><p><i>Some text</i><a href="https://www.google.com">A link</a></p><h4>Heading4</h4></body>',
        )


if __name__ == "__main__":
    unittest.main()
