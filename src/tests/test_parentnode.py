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
      node3 = ParentNode(
        "body",
        [
            LeafNode("b", "Bold text"),
        ],
      )
      self.assertEqual( # test node with many children
         "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html()
      )
      self.assertEqual(# test node with parentnode as child
         "<p>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</p>", node2.to_html()
      )
      self.assertEqual(# test node with only one child
         "<body><b>Bold text</b></body>", node3.to_html()
      )

    def test_headings(self):
      node = ParentNode(
          "h2",
          [
              LeafNode("b", "Bold text"),
              LeafNode(None, "Normal text"),
              LeafNode("i", "italic text"),
              LeafNode(None, "Normal text"),
          ],
      )
      self.assertEqual(
          node.to_html(),
          "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
      )