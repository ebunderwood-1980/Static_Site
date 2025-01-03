import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_creation(self):
        l1 = LeafNode(tag="p", value="This is a paragraph of text.")
        l2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        l3 = LeafNode(
            "a",
            "Visit my wizard tower",
            {
                "href": "https://tower.magic",
                "target": "_blank",
                "class": "magical-link",
            },
        )
        self.assertEqual(l1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(l2.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(
            l3.to_html(),
            '<a href="https://tower.magic" target="_blank" class="magical-link">Visit my wizard tower</a>',
        )


if __name__ == "__main__":
    unittest.main()
