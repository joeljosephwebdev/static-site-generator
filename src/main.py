from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
  text_node = TextNode("This is a link node", "link", "https://www.besstimett.com")
 
  print(text_node_to_html_node(text_node))

if __name__ == '__main__':
  main()