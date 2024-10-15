from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import split_nodes_delimiter

def main():
  node = TextNode(
    "This is text with a **bolded** word and **another** and now *italic* word too", "text"
  )
  new_nodes = split_nodes_delimiter([node], "**")
  new_nodes = split_nodes_delimiter(new_nodes, "*")
 
  print(new_nodes)

if __name__ == '__main__':
  main()