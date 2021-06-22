import os
import os.path as osp
import logging 
logging.basicConfig(level=logging.INFO)   #(ref) https://hwangheek.github.io/2019/python-logging/

from PIL import Image


logging.info(__file__)



def get_imlist(path):
    """    Returns a list of filenames for 
        all jpg images in a directory. """
        
    return [osp.join(path, file) for file in os.listdir(path) if file.endswith('.jpg')]