import numpy as np
import cv2
from PIL import Image
import pandas as pd
data=pd.read_csv("Data.csv")

for i in range(1,424):
    x=data["Image Name"][i-1]
    y=x[0]+x[:-4][-2:]
    imgo = cv2.imread("C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//PennFudanPed//PNGImages//"+x)
    img1 = cv2.imread("C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//PennFudanPed//PedMasks//"+x[:-4]+"_mask.png")
    n=int(data["Object No"][i-1])
    imgo[np.where((img1!=[n,n,n]).all(axis=2))]=[0,0,0]
    cv2.imwrite("img.png",imgo)
    na = cv2.imread('img.png')
    alpha = np.sum(na, axis=-1) > 0
    alpha = np.uint8(alpha * 255)
    res = np.dstack((na, alpha))
    cv2.imwrite('result.png', res)
    mi=data["Min point"][i-1]
    mi=mi.strip("(").strip(")").split()
    ma=data["Max point"][i-1]
    ma=ma.strip("(").strip(")").split()
    im = Image.open(r"result.png")
    left,top=map(int,mi)
    right,bottom=map(int,ma)
    im1 = im.crop((left, top, right, bottom))
    #im1.save("C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//objects//Person "+str(i)+".png")
    #print(i)


