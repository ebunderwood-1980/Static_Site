from block_markdown import split_blocks
import unittest


class testSplitBlocks(unittest.TestCase):
    def testStandardBlock(self):
        input_text = "# This is a heading\n\nThis is a paragraph of text.  It has some **bold** and *italic* words inside of it\n\n*This is the first list item in a list block\n*This is a list item\n*This is another list item"

        normal_text, bold_n_italic, list_block = split_blocks(input_text)

        self.assertEqual(normal_text, "# This is a heading")
        self.assertEqual(
            bold_n_italic,
            "This is a paragraph of text.  It has some **bold** and *italic* words inside of it",
        )
        self.assertEqual(
            list_block,
            "*This is the first list item in a list block\n*This is a list item\n*This is another list item",
        )

    def testNewlineHeavyBlocks(self):
        input_text = "# This is a heading\n\n\n# This is a heading, too\n\n\n\n\nThis has some **bold**"

        heading1, heading2, bold_line = split_blocks(input_text)

        self.assertEqual(heading1, "# This is a heading")
        self.assertEqual(heading2, "# This is a heading, too")
        self.assertEqual(bold_line, "This has some **bold**")

    def testWhitespaceHeavyBlocks(self):
        input_text = "      # This is a heading     \n\n        This is some text      "

        heading1, heading2 = split_blocks(input_text)

        self.assertEqual(heading1, "# This is a heading")
        self.assertEqual(heading2, "This is some text")


if __name__ == "__main__":
    unittest.main()
