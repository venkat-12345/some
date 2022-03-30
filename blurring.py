from dt_face_blur_api import FaceBlurAPI
import cv2
import numpy
fb = FaceBlurAPI(
    api_url="https://api.detectpl.com/face_blur",
    username="detect",
    password="vision-pogo@urgency_divided"
)
for i in range(1,2):
    x=str(i) if i>9 else "0"+str(i)
    img = fb.blur_path(r"PennFudanPed//PNGImages//FudanPed000"+x+".png") # Opens and runs inference on image stored in the disk



    cv2.imwrite(r"BlurrImages//bFudanPed000"+x+".png", img)
    print(i)

