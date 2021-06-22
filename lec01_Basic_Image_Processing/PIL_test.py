from PIL import Image

from CVLibs.tools import imtools


img_list = imtools.get_imglist("./data")
print(img_list)



pil_im = Image.open(img_list[1])
#pil_im.show()


copy_pil = pil_im.copy()
copy_pil.thumbnail((128,128))
#copy_pil.show()




box = (50,50,600,600)  # RoI ; (x1, y1, x2, y2)
region = pil_im.crop(box)

region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)
#pil_im.show()


out = pil_im.resize((128,128))
out = pil_im.rotate(45)  # rotate 45 in counterclockwise 
#out.show()


