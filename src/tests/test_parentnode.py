import unittest
import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the directory above
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_values(self):
      node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
      )
      self.assertEqual(
          node.tag,
          "p",
      )
      self.assertListEqual(
          node.children,
          [
              LeafNode("b", "Bold text"),
              LeafNode(None, "Normal text"),
              LeafNode("i", "italic text"),
              LeafNode(None, "Normal text"),
          ],
      )
      self.assertEqual(
          node.props,
          None,
      )

    def test_repr(self):
      node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
      )
      self.assertEqual(
          "ParentNode(p [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)] None)", repr(node)
      )

    def test_eq(self):
      node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
      )
      node2 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
      )
      self.assertEqual(node, node2)

    def test_assignment_errors(self):
       with self.assertRaises(ValueError) as context: #test where children is None
          node4 = ParentNode("p", None, None)
       self.assertEqual(str(context.exception), "parent node must have at least one child node")

       with self.assertRaises(ValueError) as context: #test where tag is None
          node4 = ParentNode(None, [LeafNode("b", "Bold text"),], None)
       self.assertEqual(str(context.exception), "parent node must have a tag")
    
    def test_to_html(self):
      node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
      )
      node2 = ParentNode(
        "p",
        [
            LeafNode(None, "Normal text"),
            ParentNode(
               "p",
              [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
              ],
            ),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
      )
      self.assertEqual(
         "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html()
      )
      self.assertEqual(
         "<p>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</p>", node2.to_html()
      )

    # def test_to_html(self):
    #    node = ParentNode("p", "This is a paragraph of text.")
    #    node2 = ParentNode("a", "Click me!", {"href": "https://www.google.com"})
    #    node3 = ParentNode(None, "Click me!", {"href": "https://www.google.com"})
    #    self.assertEqual( # standard test
    #       "<p>This is a paragraph of text.</p>", node.to_html()
    #    )
    #    self.assertEqual( # test with props
    #       '<a href="https://www.google.com">Click me!</a>', node2.to_html()
    #    )
    #    self.assertEqual( # test where tag is None
    #       "Click me!", node3.to_html() 
    #    )
      
    #    with self.assertRaises(ValueError) as context: #test where value is None
    #       node4 = ParentNode("p", None, {"font-family" : "Roboto"})
    #    self.assertEqual(str(context.exception), "parent node must have a value")
    
    # def test_props_to_html(self):
    #   node = ParentNode("a", "Click me!", {"href": "https://www.google.com", "color" : "blue"})
    #   self.assertEqual(
    #      ' href="https://www.google.com" color="blue"', node.props_to_html()
    #   )