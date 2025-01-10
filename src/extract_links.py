import re

def extract_markdown_images(text):
    images = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    match = re.findall(images, text)
    return match

def extract_markdown_links(text):
    links = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    match = re.findall(links, text)
    return match

