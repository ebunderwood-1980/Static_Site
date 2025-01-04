from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        return_string = ""
        if self.tag is None:
            raise ValueError("Parent Node must have a tag")
        elif self.children is None:
            raise ValueError("Parent node must have children")
        else:
            for child in self.children:
                return_string = f"{return_string}{child.to_html()}"
        return f"<{self.tag}>{return_string}</{self.tag}>"
