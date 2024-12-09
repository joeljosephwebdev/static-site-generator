# static-site-generator 🌐🤖

## Authors 🙋‍♂️

- [Joel Joseph](https://www.github.com/joeljosephwebdev)

## Description

This is a static site generator written in python. It creates html pages from markdown files.

## Getting Started 💫

Store all physical assets in the *static* folder. 
Add all markdown files to the *content* folder. Pages can be separated with sub-folders.

### Prerequisites 🚀

The only Prerequisites is to have python3 installed. I am specifically running Python 3.12.6.

* python version
   ```sh
    python3 --version  
    Python 3.12.6

## Usage

Run the test.sh shell script from the root folder. Make sure all tests pass.

* Running tests
  ```sh
    ./test.sh
    ..............................................................
    ----------------------------------------------------------------------
    Ran 62 tests in 0.003s

    OK


Run python3 main.py src folder to generate all web pages.

* Run main.py
  ```sh
    python3 src/main.py
    2024-10-23 23:26:49,192 - INFO - ------- Static site generator initialized -------
    2024-10-23 23:26:49,193 - INFO - Deleted file 'public/index.html' ✓
    2024-10-23 23:26:49,193 - INFO - Deleted file 'public/.DS_Store' ✓
    2024-10-23 23:26:49,194 - INFO - Deleted 'public/images' directory contents ✓
    2024-10-23 23:26:49,194 - INFO - Deleted file 'public/index.css' ✓
    2024-10-23 23:26:49,194 - INFO - Deleted file 'public/first-post/index.html' ✓
    2024-10-23 23:26:49,194 - INFO - Deleted 'public/first-post' directory contents ✓
    2024-10-23 23:26:49,194 - INFO - Deleted 'public' directory contents ✅
    2024-10-23 23:26:49,194 - INFO - All Paths verified ✅
    2024-10-23 23:26:49,195 - INFO - Copied 'static/.DS_Store' to 'public' ✓
    2024-10-23 23:26:49,195 - INFO - Copied 'static/images' to 'public' ✓
    2024-10-23 23:26:49,196 - INFO - Copied 'static/index.css' to 'public' ✓
    2024-10-23 23:26:49,196 - INFO - Copied 'static/' to 'public' ✅
    2024-10-23 23:26:49,196 - INFO - Generating page from 'src/content/index.md' to 'public' using 'template.html'
    2024-10-23 23:26:49,196 - INFO - Reading markdown from 'src/content/index.md' ✓
    2024-10-23 23:26:49,196 - INFO - Converting markdown to html ✓
    2024-10-23 23:26:49,198 - INFO - Reading template html from 'template.html' ✓
    2024-10-23 23:26:49,198 - INFO - Adding content to html template. ✓
    2024-10-23 23:26:49,198 - INFO - Writing html to 'public/index.html' ✓
    2024-10-23 23:26:49,198 - INFO - public/index.html created successfully ✅
    2024-10-23 23:26:49,198 - INFO - Creating directory public/first-post ✓
    2024-10-23 23:26:49,199 - INFO - Generating page from 'src/content/first-post/index.md' to 'public/first-post' using 'template.html'
    2024-10-23 23:26:49,199 - INFO - Reading markdown from 'src/content/first-post/index.md' ✓
    2024-10-23 23:26:49,199 - INFO - Converting markdown to html ✓
    2024-10-23 23:26:49,201 - INFO - Reading template html from 'template.html' ✓
    2024-10-23 23:26:49,203 - INFO - Adding content to html template. ✓
    2024-10-23 23:26:49,204 - INFO - Writing html to 'public/first-post/index.html' ✓
    2024-10-23 23:26:49,204 - INFO - public/first-post/index.html created successfully ✅
    2024-10-23 23:26:49,204 - INFO - ------- Site generation completed ✅ -------
    2024-10-23 23:26:49,205 - INFO - Process time 0.01s

You can run the main.sh shell script to also start a server to view all the pages.

* Running the main shell script
    ```sh
      ./main.sh

      Serving HTTP on :: port 8888 (http://[::]:8888/) ...

All logged messages are stored to *static_site.log* in the root folder.

## Cheat Sheet

This cheat sheet provides a quick reference for all the HTML and Markdown syntax you'll need to complete this project. *Feel free to bookmark this page so you can come back to it as you work on this project.*

### References

- [MarkdownGuide.org](https://www.markdownguide.org/cheat-sheet/)
- [HTML Element Reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

*Fun fact: Discord, GitHub, and ChatGPT all support Markdown messages. When you use Markdown on those platforms it will render beautifully.*

### HTML Headings

```
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
```

### Markdown Headings

```
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
```

### HTML Paragraphs

```
<p>This is a paragraph of text.</p>
```

### Markdown Paragraphs

This is a paragraph of text.

### HTML Bold

```
<p>This is a <b>bold</b> word.</p>
```

### Markdown Bold

```
This is a **bold** word.
```

### HTML Italics

```
<p>This is an <i>italic</i> word.</p>
```

### Markdown Italics

```
This is an *italic* word.
```

Note: some linting tools may autocorrect *italic* to _italic_, which is also markdown syntax for italics, but may trip you up during testing.

### HTML Links

```
This is a paragraph with a <a href="https://www.google.com">link</a>.
```

### Markdown Links

```
This is a paragraph with a [link](https://www.google.com).
```

### HTML Images

```
<img src="url/of/image.jpg" alt="Description of image">
```

### Markdown Images

```
![alt text for image](url/of/image.jpg)
```

### HTML Unordered Lists

```
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

### Markdown Unordered Lists

```
* Item 1
* Item 2
* Item 3
```

### HTML Ordered Lists

```
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ol>
```

### Markdown Ordered Lists

```
1. Item 1
2. Item 2
3. Item 3
```

### HTML Quotes

```
<blockquote>
    This is a quote.
</blockquote>
```

### Markdown Quotes

```
> This is a quote.
```

### HTML Code

```
<code>This is code</code>
```

Markdown Code
```
```This is code```
```
