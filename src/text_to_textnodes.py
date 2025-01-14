from textnode import TextNode, TextType
from split_nodes import split_nodes_link, split_nodes_image
from split_node_delimiter import split_nodes_delimiter

def text_to_textnodes(input_text):
    nodes = [TextNode(input_text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes   

