from PIL import Image
for x in range(1,97):
    i=str(x) if x>9 else "0"+str(x)
    #image_path ="C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//PennFudanPed//PNGImages//FudanPed000"+i+".png"
    image_path ="C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//PennFudanPed//PNGImages//PennPed000"+i+".png"
    image_file = Image.open(image_path)
    image_file.save("C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//Resolution//PennPed000"+i+"q95.jpg", quality=95)
    image_file.save("C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//Resolution//PennPed000"+i+"q75.jpg", quality=75)
    image_file.save("C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//Resolution//PennPed000"+i+"q50.jpg", quality=50)
    image_file.save("C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//Resolution//PennPed000"+i+"q25.jpg", quality=25)
    image_file.save("C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//Resolution//PennPed000"+i+"q1.jpg", quality=1)
