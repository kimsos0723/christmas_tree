import os
import numpy as np
from PIL import Image

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
        rgb_img = img.convert('RGB')
        pixels = rgb_img.load()
        n = common_dividor(xsize, ysize)
        factor = n[len(n)-1]
        ascii_pixel_matrix = []
        for y in range(0, ysize, factor):
            ascii_pixel_row=[]
            for x in range(0, xsize, factor):
                pixel_color_sum = [0,0,0]
                for i in range(factor):
                    for j in range(factor):
                        pixel_color_sum[0] += rgb_img.getpixel((x+j,y+i))[0]
                        pixel_color_sum[1] += rgb_img.getpixel((x+j,y+i))[1]
                        pixel_color_sum[2] += rgb_img.getpixel((x+j,y+i))[2]
                pixel_color_sum[0] = pixel_color_sum[0] // factor*factor  
                pixel_color_sum[1] = pixel_color_sum[1] // factor*factor  
                pixel_color_sum[2] = pixel_color_sum[2] // factor*factor  
                ascii_pixel_row.append(pixel_color_sum)
            ascii_pixel_matrix.append(ascii_pixel_row)
        
        
        index = 0
        new_img = Image.new('RGB',(xsize//factor+1 , ysize//factor+1))
        for i in range(ysize//factor):
            for j in range(xsize//factor):
                new_img.putpixel((j,i),tuple(ascii_pixel_matrix[i][j]))
                index += 1
        new_img.show()
        new_img.save('tree2.png')
        # ASCII = ('.', ',', ';', '!', 'v', 'l', 'L', 'F', 'E', '$', '#', '@')
        # for i in range(ysize//factor):
        #    for j in range(xsize//factor):
        #         print(ASCII[sum(ascii_pixel_matrix[i][j])//256//3])
        # print('\n')

        
   
