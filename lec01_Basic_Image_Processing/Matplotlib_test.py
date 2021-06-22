from CVLibs.tools import imtools

import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt



img_list = imtools.get_imglist("./data")
print(img_list)



pil_im = Image.open(img_list[1])
np_img = np.asarray(pil_im) # as np.array

plt.imshow(np_img) # (ref) https://www.delftstack.com/ko/howto/matplotlib/display-an-image-with-matplotlib-python/
#plt.show()


""" Some points - (x1, y1), (x2, y2), ...
"""
x = [100,100,400,400]  
y = [200,500,200,500]

plt.plot(x,y,'r*')  # plot the points with red star-markers

plt.plot(x[:2], y[:2]) # line plot connecting the first two points

plt.title(f"Plotting: '{img_list[1]}'") # add title and show the plot

#plt.axis('off')



plt.show()


