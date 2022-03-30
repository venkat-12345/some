from PIL import Image
  
for i in range(1,21):
    img1 = Image.open(r"Industrial Images//I4.jpg")
    img2 = Image.open(r"objects//Person "+str(i)+".png")
    (width,height)=img1.size
    (w,h)=img2.size
    img1.paste(img2, (width-300,height-50-h), mask = img2)
  

    img1.save(r"IB Images//4Image"+str(i)+".png")
