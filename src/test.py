from htmlnode import HTMLNode

h1 = HTMLNode(
    props={
        "href": "https://www.google.com",
        "target": "_blank",
    }
)
print(h1.props_to_html())

print(f"Node Printing: {h1}")
