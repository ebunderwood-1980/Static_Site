from textnode import TextType, TextNode
from extract_links import extract_markdown_links, extract_markdown_images

def split_nodes_link(old_nodes):
    result_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            result_nodes.append(node)
            continue
            
        links = extract_markdown_links(node.text)
        if not links:
            result_nodes.append(node)
            continue
            
        remaining_text = node.text  # Keep track of unprocessed text
        for alt, url in links:
            # Split remaining_text using current link as delimiter
            sections = remaining_text.split(f"[{alt}]({url})", 1)
            
            # Add non-empty text before the link
            if sections[0]:
                result_nodes.append(TextNode(sections[0], TextType.NORMAL))
                
            # Add the link itself
            result_nodes.append(TextNode(alt, TextType.LINK, url=url))
            
            # Update remaining_text for next iteration
            if len(sections) > 1:
                remaining_text = sections[1]
            
        # Don't forget to add any remaining text after the last link
        if remaining_text:
            result_nodes.append(TextNode(remaining_text, TextType.NORMAL))
            
    return result_nodes

     
    
def split_nodes_image(old_nodes):
    result_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            result_nodes.append(node)
            continue
            
        links = extract_markdown_images(node.text)
        if not links:
            result_nodes.append(node)
            continue
            
        remaining_text = node.text  # Keep track of unprocessed text
        for alt, url in links:
            # Split remaining_text using current link as delimiter
            sections = remaining_text.split(f"![{alt}]({url})", 1)
            
            # Add non-empty text before the link
            if sections[0]:
                result_nodes.append(TextNode(sections[0], TextType.NORMAL))
                
            # Add the link itself
            result_nodes.append(TextNode(alt, TextType.IMAGE, url=url))
            
            # Update remaining_text for next iteration
            if len(sections) > 1:
                remaining_text = sections[1]
            
        # Don't forget to add any remaining text after the last link
        if remaining_text:
            result_nodes.append(TextNode(remaining_text, TextType.NORMAL))
            
    return result_nodes


# def main():
#     node = TextNode(
#             "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#             TextType.NORMAL
#             )
#     print(split_nodes_link([node]))


# if __name__ == '__main__':
#     main()
