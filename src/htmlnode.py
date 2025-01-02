class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not Implemented")

    def props_to_html(self):
        string_accumulator = ""
        for key in self.props:
            string_accumulator = f'{string_accumulator} {
                key}="{self.props[key]}"'
        return string_accumulator

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
