import os
import numpy as np
from PIL import Image
from fractions import Fraction
# image_path = input()
image_path = "tree.gif"
common_dividors = []
def common_dividor(x,y):
    n = []
    g = np.gcd(x,y)
    for i in range(1,g+1):
        if g % i == 0:
            n.append(i)
    return n
     
with Image.open(image_path) as img:
    if img.format != "GIF":
        print("It is not a 'GIF'!")
        exit(1)
    xsize, ysize = img.size

    if img.is_animated:
        pass
    else:
        rgb_img = img.convert('RGBA')
        pixels = rgb_img.load()
        n = common_dividor(xsize, ysize)
        factor = n[len(n) // 2]
        print(xsize, ysize)
        print(Fraction(xsize, ysize))
        print(n, factor, np.gcd(xsize, ysize))

        rgb_img.save('tree2.png')

   
