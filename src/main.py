from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type
from markdown_to_html import markdown_to_html_node

def main():
  markdown = """
# Markdown syntax guide

## Headers

## Emphasis

*This text will be italic*  
_This will also be italic_

**This text will be bold**  
_This will also be bold_

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
"""

  nodes = markdown_to_html_node(markdown)

  print(nodes)

if __name__ == '__main__':
  main()