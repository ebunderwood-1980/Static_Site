import unittest

from textnode import TextNode, TextType
from split_node_delimiter import split_nodes_delimiter


class TestSplitNode(unittest.TestCase):
    def test_eq(self):
        bold_node = TextNode("This is a text with a **bolded phrase** in the middle", text_type = TextType.NORMAL)
        bold_delimited = split_nodes_delimiter([bold_node], '**', TextType.BOLD)
        answer = [
            TextNode("This is a text with a ", TextType.NORMAL),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.NORMAL),
        ]
        self.assertEqual(bold_delimited, answer)
        


if __name__ == "__main__":
    unittest.main()
