from textnode import TextNode, TextType


def main():
    print("Hello world")

    myTextNode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    yourTextNode = TextNode(
        "This is a text node", TextType.BOLD, "https://www.boot.dev"
    )

    print(myTextNode)
    print(f"Equal: {myTextNode == yourTextNode}")


if __name__ == "__main__":
    main()
