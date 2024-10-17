import re

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
        return block_type_heading
    
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