import time
import os

from logger import logging

from copystatic import copy_static
from constants import UNICODE_CHARACTERS,PATHS
from generate_page import generate_page


def main():
  logging.info(f"------- Static site generator initialized -------")
  start = time.time()
  copy_static()

  content_path = PATHS["CONTENT"]
  for file in os.listdir(content_path):
    generate_page(os.path.join(content_path, file), PATHS["TEMPLATE"], PATHS["PUBLIC"])
  end = time.time()

  logging.info(f"Process time {end - start:.2f}")
  logging.info(f"------- Site generation compelete {UNICODE_CHARACTERS["CHECK_MARK"]} -------\n")

if __name__ == '__main__':
  main()