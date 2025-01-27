from block_markdown import block_to_block_type
import unittest

class TestBlocktoBlockType(unittest.TestCase):
    def testHeadings(self):
        inputs = [
            "# Heading 1",
            "### Heading 3",
            "###### Heading 4",
            "########## This is not a heading",
            "``` this is a code block```",
            "``` def test():\n    print(Hello world)```",
            "``` ```",
            "```   ``",
            "``  ```",
            "> Quote Text",
            "> Multi-line quote\n> Hello",
            "> Not a multi-line quote\n Line two",
            "* First item\n* Second Item",
            "* First item\n- Second Item",
            "- First item\n- Second Item",
            " First item \n- Second Item",
            "* First item \n  Second item",
            "*First item",
            "1. First item\n2. Second item",
            "0. Zero\n1. First",
            "1. First\nSecond\n2. Second",
        ]

        function_results = list(map(lambda x: block_to_block_type(x), inputs))
        print(function_results)
        correct_answers = [
            'heading',
            'heading',
            'heading',
            'normal',
            'code',
            'code',
            'code',
            'normal',
            'normal',
            'quote',
            'quote',
            'normal',
            'unordered list',
            'unordered list',
            'unordered list',
            'normal',
            'normal',
            'normal',
            'ordered list',
            'normal',
            'normal',   
        ]
        self.assertEqual(function_results, correct_answers)
        

        
