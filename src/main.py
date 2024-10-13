from textnode import TextNode
from htmlnode import HTMLNode

def main():
  text_node = TextNode("This is a text node", "bold", "https://www.besstimett.com")
  html_node = HTMLNode("a", "Link", None, {"href": "https://www.besstimett.com", "target": "_blank",})
  print(html_node.props_to_html())
  # print(html_node.to_html())
  # print(text_node)

if __name__ == '__main__':
  main()