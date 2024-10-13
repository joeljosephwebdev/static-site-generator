import unittest
import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the directory above
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_values(self):
      node = LeafNode("div", "I wish I could read",)
      self.assertEqual(
          node.tag,
          "div",
      )
      self.assertEqual(
          node.value,
          "I wish I could read",
      )
      self.assertEqual(
          node.props,
          None,
      )

    def test_repr(self):
      node = LeafNode("a", "Link", {"href": "https://www.besstimett.com", "target": "_blank",})
      self.assertEqual(
          "LeafNode(a, Link, {'href': 'https://www.besstimett.com', 'target': '_blank'})", repr(node)
      )

    def test_to_html(self):
       node = LeafNode("p", "This is a paragraph of text.")
       node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
       node3 = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
       self.assertEqual( # standard test
          "<p>This is a paragraph of text.</p>", node.to_html()
       )
       self.assertEqual( # test with props
          '<a href="https://www.google.com">Click me!</a>', node2.to_html()
       )
       self.assertEqual( # test where tag is None
          "Click me!", node3.to_html() 
       )
      
       with self.assertRaises(ValueError) as context: #test where value is None
          node4 = LeafNode("p", None, {"font-family" : "Roboto"})
       self.assertEqual(str(context.exception), "leaf node must have a value")
    
    def test_props_to_html(self):
      node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "color" : "blue"})
      self.assertEqual(
         ' href="https://www.google.com" color="blue"', node.props_to_html()
      )