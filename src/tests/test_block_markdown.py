import unittest
import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the directory above
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_olist,
    block_type_ulist
)

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_types_heading(self):
        block = "# this is a heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "### this is also a heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "###this is not a heading"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "####### this is not a heading, because it has more than 6 #s"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_to_block_types_code(self):
        block = "```this is a code block```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "```\n this is also a code block\nwith multiple lines\nof code```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "```\n this is not a code block\nbecause the block was not\nproperly closed``"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
    
    def test_block_to_block_types_quote(self):
        block = "> this is a quote block"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "> this is a quote block\n> with more than one line"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "> this is not a quote block\n>because this line is missing a space after >"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
    
    def test_block_to_block_types_ulist(self):
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "- this is not an unordered list\n* because it mixes - and * characters"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_to_block_types_olist(self):
        block = "1. this is an ordered list\n2. with 2 items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "1. this is not an ordered list\n3. because it fails to increment correctly"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
        block = "4. this is not an ordered list\n5. because it does not start from 1"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_to_block_types_paragraph(self):
        block = "this is a regular paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()