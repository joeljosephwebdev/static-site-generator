import unittest
import sys
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the directory above
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from generate_page import extract_title
from logger import logging
logging.disable()

class TestExtractTitle(unittest.TestCase):
  def test_single_line(self):
    md = "# Title"
    self.assertEqual(
        extract_title(md),
        "Title"
    )

  def test_multiple_lines(self):
   md = """
# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien

* You can spend years studying the legendarium and still not understand its depths
* It can be enjoyed by children and adults alike
* Disney *didn't ruin it*
* It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Hello, World!")
}
```
"""
   self.assertEqual(
      extract_title(md),
      "Tolkien Fan Club"
    )

  def test_no_title(self):
    md = """
**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien
"""
    with self.assertRaises(Exception) as context:
      extract_title(md)
      self.assertEqual(
        context,
        "no title found in markdown ❌"
      )