from PIL import Image
from dt_face_blur_api import FaceBlurAPI
import numpy as np
import cv2
fb = FaceBlurAPI(
    api_url="https://api.detectpl.com/face_blur",
    username="detect",
    password="vision-pogo@urgency_divided"
)
for i in range(1,10):
    for j in range(21,31):
        img1 = Image.open(r"Industrial Images//I2.jpg")
        img2 = Image.open(r"objects//Person "+str(j)+".png")
        (width,height)=img2.size
        img2=img2.resize((int(width-0.1*i*width),int(height-0.1*i*height)))
        (w,h)=img1.size
        img1.paste(img2, (w-250,h-250), mask = img2)
        img1.save("image.png")
        img1 = fb.blur_path("image.png")
        print(i,j)
        cv2.imwrite(r""+str(j)+"image"+str(i)+".png",img1)
    
    
