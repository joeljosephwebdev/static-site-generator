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