import unittest

from parentnode import ParentNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        n1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            n1.to_html(),
        )

    def test_nested(self):
        inner_node = ParentNode(
            "ul", [LeafNode("li", "list item 1"),
                   LeafNode("li", "list item 2")]
        )

        outer_node = ParentNode("div", [inner_node])

        self.assertEqual(
            outer_node.to_html(),
            "<div><ul><li>list item 1</li><li>list item 2</li></ul></div>",
        )


if __name__ == "__main__":
    unittest.main()
