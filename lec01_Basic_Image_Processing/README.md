# Ch01. Basic Image Handling and Processing 

#### [contents]- handing and processing image data 
* reading 
* converting 
* scaling
* computing derivatives 
* plotting 
* saving results 



### 1. ```PIL``` - The Python Imaging Library 
<br/>

Loading image:
``` python
from PIL import Image

pil_im = Image.open('empire.jpg')

pil_im = Image.open('empire.jpg').convert('L') # cvt RGB to grayscale 
```

