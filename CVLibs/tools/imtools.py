import os
import os.path as osp
import logging 
logging.basicConfig(level=logging.INFO)   #(ref) https://hwangheek.github.io/2019/python-logging/

from PIL import Image

logging.info(f"Import from : {__file__}")

def get_imglist(path):
    """    Returns a list of filenames for 
        all jpg images in a directory. """
        
    return [osp.join(path, file) for file in os.listdir(path) if file.endswith('.jpg')]
