import os

from logger import logging
from block_markdown import markdown_to_html_node
from constants import UNICODE_CHARACTERS


def generate_pages_recursive(src_path_content, template_path, dest_dir_path):
  contents = os.listdir(src_path_content)

  if not os.path.exists(dest_dir_path):
    logging.info(f"Creating directory {dest_dir_path} {UNICODE_CHARACTERS['SMALL_CHECK_MARK']}")
    os.mkdir(dest_dir_path)

  for file in contents:
    file_path = os.path.join(src_path_content,file)

    if os.path.isfile(file_path):
      try:
        generate_page(file_path, template_path, dest_dir_path) 
        logging.info(f"{os.path.join(dest_dir_path, file[:-3]+'.html')} created successfully {UNICODE_CHARACTERS['CHECK_MARK']}") 
      except Exception as e:
        logging.error(f"Error generating {file_path} - {e}")
        raise Exception(e)
    else:
      generate_pages_recursive(file_path, template_path, os.path.join(dest_dir_path, file))

def generate_page(src_path : str, template_path : str, dst_path : str):
  logging.info(f"Generating page from '{src_path}' to '{dst_path}' using '{template_path}'")

  try:
    with open(src_path, 'r') as src:
      logging.info(f"Reading markdown from '{src_path}' {UNICODE_CHARACTERS['SMALL_CHECK_MARK']}")
      markdown = src.read()
  except FileNotFoundError:
    logging.error(f"file not found '{src_path}' {UNICODE_CHARACTERS['FAIL_MARK']}")
    raise FileNotFoundError(f"file not found '{src_path}'")
  except Exception as e:
    logging.error(f"an error occurred reading file '{src_path}' - {e} {UNICODE_CHARACTERS['FAIL_MARK']}")
    raise Exception(e)
  
  logging.info(f"Converting markdown to html {UNICODE_CHARACTERS['SMALL_CHECK_MARK']}")
  html_node = markdown_to_html_node(markdown)
  content = html_node.to_html()

  try:
    with open(template_path, 'r') as file:
      logging.info(f"Reading template html from '{template_path}' {UNICODE_CHARACTERS['SMALL_CHECK_MARK']}")
      template = file.read()
  except FileNotFoundError:
    logging.error(f"file not found '{template_path}' {UNICODE_CHARACTERS['FAIL_MARK']}")
    raise FileNotFoundError(f"file not found '{template_path}'")
  except Exception as e:
    logging.error(f"an error occurred reading file '{template_path}' - {e} {UNICODE_CHARACTERS['FAIL_MARK']}")
    raise Exception(e)
  
  logging.info(f"Adding content to html template. {UNICODE_CHARACTERS['SMALL_CHECK_MARK']}")
  html = template.replace("{{ Title }}", extract_title(markdown))
  html = html.replace("{{ Content }}", content)
  
  # Define the destination file path by changing the extension
  file_name = os.path.basename(src_path)
  dst_file = os.path.join(dst_path, os.path.splitext(file_name)[0] + '.html')

  logging.info(f"Writing html to '{dst_file}' {UNICODE_CHARACTERS['SMALL_CHECK_MARK']}")
  with open(dst_file, 'w') as dst_file_handle:
    dst_file_handle.write(html)

def extract_title(markdown : str) -> str:
    # Split the input text into lines
    lines = markdown.splitlines()
    
    # Iterate over the lines
    for line in lines:
        # Check if the line starts with "# "
        if line.startswith("# "):
            # Return the line without the "# "
            return line[2:]  # Strip away the "# "
    
    logging.error(f"no title found in markdown {UNICODE_CHARACTERS['FAIL_MARK']}")
    raise Exception(f"no title found in markdown {UNICODE_CHARACTERS['FAIL_MARK']}")