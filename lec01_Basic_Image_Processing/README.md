# Ch01. Basic Image Handling and Processing 

#### [contents]- handing and processing image data 
* reading 
* converting 
* scaling
* computing derivatives 
* plotting 
* saving results 



### 1. ```PIL``` - The Python Imaging Library 
* [colab](https://colab.research.google.com/github/DoranLyong/Programming-ComputerVision-Python/blob/main/lec01_Basic_Image_Processing/PIL_test.ipynb) 
<br/>

Loading image:
``` python
from PIL import Image

pil_im = Image.open('empire.jpg')

pil_im = Image.open('empire.jpg').convert('L') # cvt RGB to grayscale 
```

Getting image data list: 
```python 
def get_imglist(path):
    """    Returns a list of filenames for 
        all jpg images in a directory. """
        
    return [osp.join(path, file) for file in os.listdir(path) if file.endswith('.jpg')]

```


Creating [Thumbnails](https://pillow.readthedocs.io/en/stable/reference/Image.html):
```python
pil_im.thumbnail((128,128))
``` 

Copy and Paste Regions:
```python
box = (100,100,400,400)  # RoI ; (x1, y1, x2, y2)
region = pil_im.crop(box)

region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)
```

Resize and Rotate:
```python
out = pil_im.resize((128,128))

out = pil_im.rotate(45)  # rotate 45 in counterclockwise 
```

### 2. ```Matplotlib``` - [(colab)](https://colab.research.google.com/github/DoranLyong/Programming-ComputerVision-Python/blob/main/lec01_Basic_Image_Processing/Matplotlib_test.ipynb#scrollTo=6vyAV7gUEATO)
* working with mathematics
* plotting graphs 
* drawing points, lines, and
curves on images