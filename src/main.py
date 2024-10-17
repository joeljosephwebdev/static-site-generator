from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link

def main():
  node = TextNode(
      "This is text with a link ![to besstime](https://www.besstimett.com) and ![to instagram](https://www.instagram.com/besstimett)",
      "text",
  )
  node2 = TextNode(
      "This is text with a link  and ",
      "text",
  )
  new_nodes = split_nodes_image([node, node2])

  print(new_nodes)

# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to besstime", TextType.LINK, "https://www.besstimett.com"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to instagram", TextType.LINK, "https://www.instagram.com/besstimett"
#     ),
# ]

if __name__ == '__main__':
  main()