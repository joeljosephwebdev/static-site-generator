import re

from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.splitlines()

    # check for heading they begin with 1-6 #'s followed by a space
    heading_match = re.match(r'^(#{1,6})\s', block)
    if heading_match and len(lines) == 1:
        return f"{block_type_heading}"
    
    # check for code blocks they begin and end with ```
    if block.startswith("```") and block.endswith("```"):
        return block_type_code

    # check for quote block, every line begins with >
    if all(line.startswith("> ") for line in lines):
        return block_type_quote

    # check unordered list, every line begins with either * or - followed by a space
    if is_unordered_list(lines):
        return block_type_ulist

    # check for ordered list block, every line begins with number followed by a . and space
    if is_ordered_list(lines):
        return block_type_olist

    # if none of the above, return paragraph
    return block_type_paragraph

def is_unordered_list(lines):
    markers = set() # we use a set to track the start of every line
    for line in lines:
        if line.startswith("* "):
            markers.add("*")
        elif line.startswith("- "):
            markers.add("-")
        else:
            return False # return false if a line begins with a character other than - or *

    return len(markers) == 1 # return true if the set only contains * or -

def is_ordered_list(lines):
    for i, line in enumerate(lines):
        # Check if the line starts with the correct pattern
        match = re.match(r'^\d+\.\s', line)
    if not match:
        return False  # Return False if the line doesn't start correctly
    
    # Check if the numbers are in the correct order
    number = int(line.split('.')[0])  # Extract the number before the dot
    if number != i + 1:
        return False  # Numbers must be sequential starting from 1

    return True  # Valid ordered list

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)