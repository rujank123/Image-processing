# from PIL import Image as im
# import numpy as np
# i = im.open('t.jpg')
# ir = np.asarray(i)
# print(ir)


# # convert rgb into gray code
# image = im.open("index.png")
# image = im.open("index.png").convert("LA")
# image.save("greyscale.png")
# image = im.open("greyscale.png")
# print(list(image.getdata()))
# print("Rujan Kharbuja")

# '''conveerting normal image into negative image'''
from PIL import Image, ImageDraw
import PIL.ImageOps
image = Image.open("t.jpeg")
img_draw = ImageDraw.Draw(image)
img_draw.text((20,250), "RUJAN KHARBUJA" , fill = "white")
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save("inverted4.jpeg")