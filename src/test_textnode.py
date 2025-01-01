import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node3)

    def test_notEq(self):
        node = TextNode("Hi", TextType.NORMAL, "www.boot.dev")
        node2 = TextNode("Hi", TextType.BOLD, "www.boot.dev")
        node3 = TextNode("Hi", TextType.NORMAL, "www.pornmd.com")
        node4 = TextNode("Hello", TextType.ITALIC, "www.pornmd.com")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)


if __name__ == "__main__":
    unittest.main()
