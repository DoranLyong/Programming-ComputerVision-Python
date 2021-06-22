import os
import logging 
logging.basicConfig(level=logging.INFO)   #(ref) https://hwangheek.github.io/2019/python-logging/

from PIL import Image


logging.info(__file__)



def get_imlist(path):
    """    Returns a list of filenames for 
        all jpg images in a directory. """
        
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]