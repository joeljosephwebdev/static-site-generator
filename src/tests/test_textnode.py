import unittest
import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the directory above
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from textnode import TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://www.besstimett.com")
        node2 = TextNode("This is a text node", "bold", "https://www.besstimett.com")
        self.assertEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a txt node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://www.besstimett.com")
        node2 = TextNode("This is a text node", "bold", "https://bosstimett.com")
        self.assertNotEqual(node, node2)
    
    def test_empty_text_eq(self):
      node = TextNode("", "image")
      node2 = TextNode("", "image")
      self.assertEqual(node, node2)
    
    def test_incorrect_text_type(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("This is a node", "Invalid Type")
        self.assertEqual(str(context.exception), "Invalid text_type: 'Invalid Type'. Must be one of: ['text', 'bold', 'italic', 'code', 'link', 'image'].")

    def test_repr(self):
      node = TextNode("This is a text node", "text", "https://www.besstimett.com")
      self.assertEqual(
          "TextNode(This is a text node, text, https://www.besstimett.com)", repr(node)
      ) 

class TestTextNodeToHTMLNode(unittest.TestCase):
  def test_text(self):
      node = TextNode("This is a text node", "text")
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, None)
      self.assertEqual(html_node.value, "This is a text node")

  def test_image(self):
      node = TextNode("This is an image", "image", "https://www.besstimett.com")
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "img")
      self.assertEqual(html_node.value, "")
      self.assertEqual(
          html_node.props,
          {"src": "https://www.besstimett.com", "alt": "This is an image"},
      )

  def test_bold(self):
      node = TextNode("This is bold", "bold")
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "strong")
      self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()