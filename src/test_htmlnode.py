import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_creation(self):
        h1 = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )

        h2 = HTMLNode("tag", "value", [], None)
        self.assertEqual(
            h1.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )


if __name__ == "__main__":
    unittest.main()
