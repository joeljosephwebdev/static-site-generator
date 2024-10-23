from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
  def __init__(self, text : str, text_type :str, url=None):
    self._text_type = None
    self.text = text
    self.text_type = text_type
    self.url = url

  @property 
  def text_type(self):
    return self._text_type
  
  @text_type.setter #validation for text_type value
  def text_type(self, value: str):
    if value.lower() not in [text_type.value for text_type in TextType]:
        raise ValueError(f"Invalid text_type: '{value}'. Must be one of: {[text_type.value for text_type in TextType]}.")
    self._text_type = value.lower()

  # Overload == comparator method. This method Compares two TextNodes and return True if all attributes are the same
  def __eq__(self, other):
    return (self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url)
  
  # Overload print method. This method returns a string representation of a TextNode formatted "TextNode(properties)"
  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
  match text_node.text_type:
    case "text":
      return LeafNode(None, text_node.text, None)
    case "bold":
      return LeafNode("strong", text_node.text, None)
    case "italic":
      return LeafNode("em", text_node.text, None)
    case "code":
      return LeafNode("code", text_node.text, None)
    case "link":
      return LeafNode("a", text_node.text, {"href" : text_node.url})
    case "image":
      return LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text})
    case _:
      raise ValueError(f"Invalid text type {text_node.text_type}")