import numpy as np
import cv2
from colorthief import ColorThief
from PIL import Image

def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b)

for i in range(2,3):
    x=str(i) if i>9 else "0"+str(i)
    imgo = cv2.imread("C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//PennFudanPed//PNGImages//FudanPed000"+x+".png")
    img1 = cv2.imread("C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//PennFudanPed//PedMasks//FudanPed000"+x+"_mask.png")


    imgo[np.where((img1!=[1,1,1]).all(axis=2))]=[0,0,0]
    cv2.imwrite("img.png",imgo)
    c=ColorThief("img.png")
    d=c.get_color(quality=1)
   
    print(rgb_to_hex(d[0],d[1],d[2]))


