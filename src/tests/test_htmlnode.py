import unittest
import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the directory above
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

  def test_values(self):
    node = HTMLNode("div", "I wish I could read",)
    self.assertEqual(
        node.tag,
        "div",
    )
    self.assertEqual(
        node.value,
        "I wish I could read",
    )
    self.assertEqual(
        node.children,
        None,
    )
    self.assertEqual(
        node.props,
        None,
    )

  def test_repr(self):
      node = HTMLNode("a", "Link", None, {"href": "https://www.besstimett.com", "target": "_blank",})
      self.assertEqual(
          "HTMLNode(a, Link, None, {'href': 'https://www.besstimett.com', 'target': '_blank'})", repr(node)
      )
  
  def test_to_html(self):
     node = HTMLNode("a", "Link", None, {"href": "https://www.besstimett.com", "target": "_blank",})
     with self.assertRaises(NotImplementedError) as context:
        node.to_html()
     self.assertIn(str(context.exception), "to_html method not implemented")
  
  def test_props_to_html(self):
     node = HTMLNode("a", "Link", None, {"href": "https://www.besstimett.com", "target": "_blank",})
     self.assertEqual(
        'href="https://www.besstimett.com" target="_blank"', node.props_to_html()
     )
    
  def test_props_to_html_empty(self):
    node = HTMLNode("a", "Link", None, None)
    self.assertEqual(
      "", node.props_to_html()
    )
    
      