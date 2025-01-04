from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        props_accumulator = ""
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag is None:
            return self.value
        else:
            if self.props:
                for key in self.props:
                    props_accumulator = f'{props_accumulator} {
                        key}="{self.props[key]}"'
                return f"<{self.tag}{props_accumulator}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
