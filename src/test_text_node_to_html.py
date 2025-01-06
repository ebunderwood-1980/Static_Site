import unittest
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType
    
class TestConversionNode(unittest.TestCase):
    def test_creation(self):
        tn_bold = TextNode('This is bold text', TextType.BOLD)
        tn_text = TextNode('This is regular text', TextType.NORMAL)  
        tn_italic = TextNode('This is italic text', TextType.ITALIC) 
        tn_code = TextNode('This is a block of code', TextType.CODE) 
        tn_image = TextNode('This is an image', TextType.IMAGE, url='www.image.com')  
        tn_link = TextNode('This is a Link', TextType.LINK, url = 'www.link.com') 

        ln_bold = text_node_to_html_node(tn_bold)
        ln_normal = text_node_to_html_node(tn_text) 
        ln_italic = text_node_to_html_node(tn_italic)
        ln_code = text_node_to_html_node(tn_code) 
        ln_link = text_node_to_html_node(tn_link)
        ln_image = text_node_to_html_node(tn_image)

        self.assertEqual(ln_bold.tag, 'b')
        self.assertEqual(ln_normal.value, 'This is regular text') 
        self.assertEqual(ln_italic.tag, 'i')
        self.assertEqual(ln_code.tag, 'code') 
        self.assertEqual(ln_link.props['href'], 'www.link.com') 

        





if __name__ == "__main__":
    unittest.main()
