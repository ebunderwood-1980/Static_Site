from split_nodes import split_nodes_link, split_nodes_image
import unittest
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_links(self):

        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)         
        new_nodes = split_nodes_link([node])
        answer = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_nodes, answer)        

    def test_images(self):
        node = TextNode("This is text with a link ![my asshole](https://www.myasshole.com)", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
    


if __name__ == '__main__':
    unittest.main()
