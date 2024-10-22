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
    block_type_ulist,
    markdown_to_html_node
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
        block = "###this is not a heading, because there is no space after the #s"
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

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <strong>bolded</strong> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <strong>bolded</strong> paragraph text in a p tag here</p><p>This is another paragraph with <em>italic</em> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <em>more</em> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_all(self):
      md = """
# Markdown syntax guide

## Headers

###### Emphasis

*This text will be italic*  
_This will also be italic_

**This text will be bold**  
__This will also be bold__

You **can** combine them

## Lists

### Unordered

* Item 1
* Item 2
* Item 2a
* Item 2b

### Ordered

1. Item 1
2. Item 2
3. Item 3

> here is a block
> of quotes
> with multiple lines


```
code
with lines
```
"""
      node = markdown_to_html_node(md)
      html = node.to_html()
      self.assertEqual(
          html,
          """<div><h1>Markdown syntax guide</h1><h2>Headers</h2><h6>Emphasis</h6><p><em>This text will be italic</em><em>This will also be italic</em></p><p><strong>This text will be bold</strong><strong>This will also be bold</strong></p><p>You <strong>can</strong> combine them</p><h2>Lists</h2><h3>Unordered</h3><ul><li>Item 1</li><li>Item 2</li><li>Item 2a</li><li>Item 2b</li></ul><h3>Ordered</h3><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol><blockquote>here is a block of quotes with multiple lines</blockquote><pre><code>code
with lines
</code></pre></div>""",
      )

if __name__ == "__main__":
    unittest.main()