import os
import shutil
from logger import logging

from constants import PATHS, UNICODE_CHARACTERS

# copy all contents from the static folder to the public folder
def copy_static():
#create public folder if it doesn't exist else delete its contents
  if not os.path.exists(PATHS['PUBLIC']) : 
     os.mkdir("public") 
     logging.info(f"Created 'public' directory {UNICODE_CHARACTERS['CHECK_MARK']}")
  else : 
     delete_directory_contents(PATHS['PUBLIC'])

  verify_paths()
  copy_directory_contents(PATHS['STATIC'], PATHS['PUBLIC'])

def verify_paths(): # verify all necessary directories are accessable
    for path in PATHS.values(): 
        if not check_path_permissions(path):
            try :
               os.mkdir(path)
            except Exception as e :
               permission_error_message = f"Failed to access directory '{path}' {UNICODE_CHARACTERS['FAIL_MARK']}"
               logging.error(permission_error_message)
               raise Exception(permission_error_message)
    logging.info(f"All Paths verified {UNICODE_CHARACTERS['CHECK_MARK']}") 

def check_path_permissions(path): 
   return (
            os.path.exists(path) # path exists
            and os.access(path, os.R_OK) # app has read access
            and os.access(path, os.W_OK) # app has write access
          )

def delete_directory_contents(directory_path, is_top_level = True):
   directory_files = os.listdir(directory_path)
   for file in directory_files:
      file_path = os.path.join(directory_path, file)
      if os.path.isfile(file_path):
        os.remove(file_path)
        logging.info(f"Deleted file '{file_path}' {UNICODE_CHARACTERS['SMALL_CHECK_MARK']}")
      else:
         delete_directory_contents(file_path, is_top_level = False)
         os.rmdir(file_path)
         logging.info(f"Deleted '{file_path}' directory contents {UNICODE_CHARACTERS['SMALL_CHECK_MARK']}")
    
   if is_top_level:
    logging.info(f"Deleted '{directory_path}' directory contents {UNICODE_CHARACTERS['CHECK_MARK']}")

def copy_directory_contents(src_path, dst_path, is_to_level = True):
  src_files = os.listdir(src_path)
  
  for file in src_files:
     file_path = os.path.join(src_path,file)
     if os.path.isfile(file_path):
        shutil.copy(file_path,dst_path)
        logging.info(f"Copied '{file_path}' to '{dst_path}' {UNICODE_CHARACTERS['SMALL_CHECK_MARK']}")
     else:
        new_dst_directory = os.path.join(dst_path,file)
        os.mkdir(new_dst_directory)
        copy_directory_contents(file_path, new_dst_directory, is_to_level = False)
        logging.info(f"Copied '{file_path}' to '{dst_path}' {UNICODE_CHARACTERS['SMALL_CHECK_MARK']}")
  
  if is_to_level:
     logging.info(f"Copied '{src_path}' to '{dst_path}' {UNICODE_CHARACTERS['CHECK_MARK']}")