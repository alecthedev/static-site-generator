from htmlnode import LeafNode


class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target) -> bool:
        return (
            self.text == target.text
            and self.text_type == target.text_type
            and self.url == target.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self, text_node):
        match text_node.text_type:
            case "text":
                return LeafNode(None, text_node.text)
            case "bold":
                return LeafNode("b", text_node.text)
            case "italic":
                return LeafNode("i", text_node.text)
            case "code":
                return LeafNode("code", text_node.text)
            case "link":
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case "image":
                return LeafNode(
                    "img", "", {"src": text_node.url, "alt": text_node.text}
                )
        raise ValueError(f"Invalid TextNode type: {text_node.text_type}")
