import re

from textnode import TextNode


def split_nodes_delimiter(old_nodes : list, delimiter : str):
    new_nodes = []
    type = ""

    match delimiter:
        case "`":
            type = "code"
        case "*":
            type = "italic"
        case "**":
            type = "bold"

    for old_node in old_nodes:
        if old_node.text_type != "text": # if the node type is not text then it should not need to be converted
            new_nodes.append(old_node)
        elif old_node.text.count(delimiter) % 2 != 0: # Check for unclosed delimiters
            raise ValueError("Invalid markdown, formatted section not closed")
        else: 
            parts = [
                TextNode(part, type if i % 2 == 1 else "text")  # add a TextNode to the list with the text and text_type for non-empty parts
                for i, part in enumerate(old_node.text.split(delimiter))
                if part.strip() or len(part) > 0  # Check if the part is non-empty or has leading/trailing spaces
            ]
            new_nodes.extend(parts)
    
    return new_nodes 

def split_nodes_image(old_nodes):
    result = []

    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(text)
        parts = []
        last_index = 0

        for alt_text, image_url in images:
            image_start = text.index(f'![{alt_text}]')
            image_end = image_start + len(f'![{alt_text}]({image_url})')

            # Add text before the link
            if last_index < image_start:
                parts.append(TextNode(text[last_index:image_start], "text"))

            # Add the link text
            parts.append(TextNode(alt_text, "image", image_url))

            # Update the last index
            last_index = image_end

        # Add any remaining text after the last link
        if last_index < len(text):
            parts.append(TextNode(text[last_index:], "text"))

        result.extend(parts)

    return result

def split_nodes_link(old_nodes):
    result = []

    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(text)
        parts = []
        last_index = 0

        for link_text, link_url in links:
            link_start = text.index(f'[{link_text}]')
            link_end = link_start + len(f'[{link_text}]({link_url})')

            # Add text before the link
            if last_index < link_start:
                parts.append(TextNode(text[last_index:link_start], "text"))

            # Add the link text
            parts.append(TextNode(link_text, "link", link_url))

            # Update the last index
            last_index = link_end

        # Add any remaining text after the last link
        if last_index < len(text):
            parts.append(TextNode(text[last_index:], "text"))

        result.extend(parts)

    return result

def extract_markdown_images(text):
    # Regular expression to match the markdown image syntax
    pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    # Regular expression to match the markdown image syntax
    pattern = r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)'
    matches = re.findall(pattern, text)
    return matches