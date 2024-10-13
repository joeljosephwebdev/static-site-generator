from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
  leaf1 = LeafNode("p", "This is a paragraph of text.")
  leaf2 = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
  print(leaf1.to_html())
  print(leaf2.to_html())


if __name__ == '__main__':
  main()