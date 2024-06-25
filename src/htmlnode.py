class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        return (
            "".join(f' {key}="{val}"' for key, val in self.props.items())
            if self.props != None
            else ""
        )

    def __repr__(self) -> str:
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {len(self.children) if self.children != None else 0}, Properties: {len(list(self.props)) if self.props != None else 0})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Leafnode value cannot be None")
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode tag cannot be None")
        if self.children is None:
            raise ValueError("ParentNode children cannot be None")

        return f"<{self.tag}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"

