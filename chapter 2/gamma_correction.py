import numpy as np
from PIL import Image

import matplotlib.pyplot as plt 

gray_img = Image.open('b.jpg').convert("LA")
gray_img.save("bgray.png")
row = gray_img.size[0]
col = gray_img.size[1]
gamma1 = 0.9
gamma2 = 2.5
result_img1 = Image.new("L", (row, col))
result_img2 = Image.new("L", (row, col))
for x in range(1 , row):
    for y in range(1, col):
        value = pow(gray_img.getpixel((x,y))[0]/255,(1/gamma1))*255
        if value >= 255 :
            value = 255
        result_img1.putpixel((x,y), int(value))
        value = pow(gray_img.getpixel((x,y))[0]/255,(1/gamma2))*255
        if value >= 255 :
            value = 255
        result_img2.putpixel((x,y), int(value))
result_img1.save("gamma_088.png")
result_img2.save("gamma_115.png")

# plt.figure(figsize=(15,10))
# y = gray_img.histogram()
# y = y[0:256]
# x = np.arange(len(y))
# plt.subplot(221)
# plt.title("lenna gray ")
# plt.bar(x, y)

# plt.subplot(222)
# y = result_img1.histogram()
# x = np.arange(len(y))
# plt.title("gamma 0.88")
# plt.bar(x, y)

# plt.subplot(223)
# y = result_img2.histogram()
# x = np.arange(len(y))
# plt.title("gamma 1.15")
# plt.bar(x, y)

# fig = plt.gcf()
# plt.show()

fig.savefig('gamma_correction.jpg')