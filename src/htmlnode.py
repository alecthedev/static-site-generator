class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str: 
        #output = ""
        #for key in props:
        #   output += f' {key}="{self.props[key]}"'
        #return output
        return ''.join(f' {key}="{val}"' for key, val in self.props.items()) if self.props != None else ""

    def __repr__(self) -> str:
        return f'HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {len(self.children) if self.children != None else 0}, Properties: {len(list(self.props)) if self.props != None else "0"})'
