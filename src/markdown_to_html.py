from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type


# convert markdown to blocks
# then get the type of each block
# recursively check each block
# any block with more than one line becomes a parentnode else they are a leafnode
# and convert each line into a text node with text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) # markdown to blocks
    html = ParentNode("div",[])

    for block in blocks:
        if block_to_block_type(block) == "paragraph":
            html.children.append(ParentNode("p",block_to_nodes(block)))
        if block_to_block_type(block) == "heading":
            html.children.append(ParentNode("h",block_to_nodes(block)))
        if block_to_block_type(block) == "code":
            html.children.append(ParentNode("code",block_to_nodes(block)))
        if block_to_block_type(block) == "quote":
            html.children.append(ParentNode("blockquote",block_to_nodes(block)))
        if block_to_block_type(block) == "ordered_list":
            html.children.append(ParentNode("ol",block_to_nodes(block)))
        if block_to_block_type(block) == "unordered_list":
            html.children.append(ParentNode("ul",block_to_nodes(block)))
    
    return html

def block_to_nodes(block):
    children = []

    for line in block.splitlines():
        children.append(line)
    
    return children

def build_parent_node(block : str, block_type : str): #recursive function that takes a block and builds a parent node with a list of child nodes
    pass

# def block_to_html(block : str, block_type : str):
#     match block_type:
#         case "heading" :
#             return f"<h>{block}</h>"
#         case "code" :
#             return f"<code>{block}</code>"
#         case "quote" :
#             return f"<blockquote>{block}</blockquote>"
#         case "ordered_list" :
#             return f"<ol>{block}</ol>"
#         case "unordered_list" :
#             return f"<ul>{block}</ul>"
#         case _:
#             return f"<p>{block}</p>"
            
ParentNode(
    'div', 
    [
        ParentNode('h', ['# Markdown syntax guide'], 'None'), 
        ParentNode('h', ['## Headers'], 'None'), 
        ParentNode('h', ['## Emphasis'], 'None'), 
        ParentNode('p', ['*This text will be italic*  ', '_This will also be italic_'], 'None'), 
        ParentNode('p', ['**This text will be bold**  ', '_This will also be bold_'], 'None'), 
        ParentNode('p', ['You **can** combine them'], 'None'), 
        ParentNode('h', ['## Lists'], 'None'), 
        ParentNode('h', ['### Unordered'], 'None'), 
        ParentNode('ul', ['* Item 1', '* Item 2', '* Item 2a', '* Item 2b'], 'None'), 
        ParentNode('h', ['### Ordered'], 'None'), 
        ParentNode('ol', ['1. Item 1', '2. Item 2', '3. Item 3'], 'None')
     ], 
     'None')