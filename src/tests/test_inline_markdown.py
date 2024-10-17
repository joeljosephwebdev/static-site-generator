import unittest
import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the directory above
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_link,
    split_nodes_image,
    extract_markdown_links,
    extract_markdown_images,
)

from textnode import TextNode


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", "text")
        new_nodes = split_nodes_delimiter([node], "**")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", "text"
        )
        new_nodes = split_nodes_delimiter([node], "**")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", "text"
        )
        new_nodes = split_nodes_delimiter([node], "**")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded word", "bold"),
                TextNode(" and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*")
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", "text")
        new_nodes = split_nodes_delimiter([node], "**")
        new_nodes = split_nodes_delimiter(new_nodes, "*")
        self.assertListEqual(
            [
                TextNode("bold", "bold"),
                TextNode(" and ", "text"),
                TextNode("italic", "italic"),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_unclosed_delim(self):
        node = TextNode("This test has a **bold** word and an unclosed *italic word", "text")
        new_nodes = split_nodes_delimiter([node], "**")
        with self.assertRaises(ValueError) as context:
            new_nodes = split_nodes_delimiter([node], "*")
        self.assertEqual(str(context.exception), "Invalid markdown, formatted section not closed")


    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://besstimett.com) and [another link](https://blog.besstimett.com)"
        )
        self.assertListEqual(
            [
                ("link", "https://besstimett.com"),
                ("another link", "https://blog.besstimett.com"),
            ],
            matches,
        )

    def test_extract_markdown_images_with_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://besstimett.com)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_with_images(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://besstimett.com) and [another link](https://blog.besstimett.com) and ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [
                ("link", "https://besstimett.com"),
                ("another link", "https://blog.besstimett.com"),
            ],
            matches,
        )


    def test_split_image(self):
            node = TextNode(
                "This is text with an ![alt_text](https://i.imgur.com/zjjcJKZ.png)",
                "text",
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", "text"),
                    TextNode("alt_text", "image", "https://i.imgur.com/zjjcJKZ.png"),
                ],
                new_nodes,
            )

    def test_split_image_single(self):
        node = TextNode(
            "![alt_text](https://www.example.COM/IMAGE.PNG)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("alt_text", "image", "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            "text",
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", "text"),
                TextNode(
                    "second image", "image", "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link(self):
            node = TextNode(
                "This is text with an [besstime](https://besstimett.com)",
                "text",
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", "text"),
                    TextNode("besstime", "link", "https://besstimett.com"),
                ],
                new_nodes,
            )

    def test_split_link_single(self):
        node = TextNode(
            "[besstime](besstimett.com)",
            "text",
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("besstime", "link", "besstimett.com"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [besstime](https://besstimett.com) and [besstime blog](https://blog.besstimett.com) with text that follows",
            "text",
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("besstime", "link", "https://besstimett.com"),
                TextNode(" and ", "text"),
                TextNode("besstime blog", "link", "https://blog.besstimett.com"),
                TextNode(" with text that follows", "text"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
