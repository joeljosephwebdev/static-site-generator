import time

from logger import logging

from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node
from copystatic import copy_static
from constants import UNICODE_CHARACTERS


def main():
  logging.info(f"------- Static site generator initialized -------")
  start = time.time()
  copy_static()
  end = time.time()
  logging.info(f"Process time {end - start:.2f}")
  logging.info(f"------- Site generation compelete {UNICODE_CHARACTERS["CHECK_MARK"]} -------\n")

if __name__ == '__main__':
  main()