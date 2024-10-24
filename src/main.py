import time

from logger import logging

from copystatic import copy_static
from constants import UNICODE_CHARACTERS,PATHS
from generate_page import generate_pages_recursive

def main():
  logging.info(f"------- Static site generator initialized -------")
  start = time.time()
  copy_static()

  logging.info
  generate_pages_recursive(PATHS["CONTENT"], PATHS["TEMPLATE"], PATHS["PUBLIC"])
  end = time.time()

  logging.info(f"------- Site generation completed {UNICODE_CHARACTERS["CHECK_MARK"]} -------")
  logging.info(f"Process time {end - start:.2f}s\n")

if __name__ == '__main__':
  main()