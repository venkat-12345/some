from urllib import request
l=['FudanPed00001.png', 'FudanPed00002.png', 'FudanPed00003.png', 'FudanPed00004.png', 'FudanPed00005.png', 'FudanPed00006.png', 'FudanPed00007.png', 'FudanPed00008.png', 'FudanPed00009.png', 'FudanPed00010.png', 'FudanPed00011.png', 'FudanPed00012.png', 'FudanPed00013.png', 'FudanPed00014.png', 'FudanPed00015.png', 'FudanPed00016.png', 'FudanPed00017.png', 'FudanPed00018.png', 'FudanPed00019.png', 'FudanPed00020.png', 'FudanPed00021.png', 'FudanPed00022.png', 'FudanPed00023.png', 'FudanPed00024.png', 'FudanPed00025.png', 'FudanPed00026.png', 'FudanPed00027.png', 'FudanPed00028.png', 'FudanPed00029.png', 'FudanPed00030.png', 'FudanPed00031.png', 'FudanPed00032.png', 'FudanPed00033.png', 'FudanPed00034.png', 'FudanPed00035.png', 'FudanPed00036.png', 'FudanPed00037.png', 'FudanPed00038.png', 'FudanPed00039.png', 'FudanPed00040.png', 'FudanPed00041.png', 'FudanPed00042.png', 'FudanPed00043.png', 'FudanPed00044.png', 'FudanPed00045.png', 'FudanPed00046.png', 'FudanPed00047.png', 'FudanPed00048.png', 'FudanPed00049.png', 'FudanPed00050.png', 'FudanPed00051.png', 'FudanPed00052.png', 'FudanPed00053.png', 'FudanPed00054.png', 'FudanPed00055.png', 'FudanPed00056.png', 'FudanPed00057.png', 'FudanPed00058.png', 'FudanPed00059.png', 'FudanPed00060.png', 'FudanPed00061.png', 'FudanPed00062.png', 'FudanPed00063.png', 'FudanPed00064.png', 'FudanPed00065.png', 'FudanPed00066.png', 'FudanPed00067.png', 'FudanPed00068.png', 'FudanPed00069.png', 'FudanPed00070.png', 'FudanPed00071.png', 'FudanPed00072.png', 'FudanPed00073.png', 'FudanPed00074.png', 'PennPed00001.png', 'PennPed00002.png', 'PennPed00003.png', 'PennPed00004.png', 'PennPed00005.png', 'PennPed00006.png', 'PennPed00007.png', 'PennPed00008.png', 'PennPed00009.png', 'PennPed00010.png', 'PennPed00011.png', 'PennPed00012.png', 'PennPed00013.png', 'PennPed00014.png', 'PennPed00015.png', 'PennPed00016.png', 'PennPed00017.png', 'PennPed00018.png', 'PennPed00019.png', 'PennPed00020.png', 'PennPed00021.png', 'PennPed00022.png', 'PennPed00023.png', 'PennPed00024.png', 'PennPed00025.png', 'PennPed00026.png', 'PennPed00027.png', 'PennPed00028.png', 'PennPed00029.png', 'PennPed00030.png', 'PennPed00031.png', 'PennPed00032.png', 'PennPed00033.png', 'PennPed00034.png', 'PennPed00035.png', 'PennPed00036.png', 'PennPed00037.png', 'PennPed00038.png', 'PennPed00039.png', 'PennPed00040.png', 'PennPed00041.png', 'PennPed00042.png', 'PennPed00043.png', 'PennPed00044.png', 'PennPed00045.png', 'PennPed00046.png', 'PennPed00047.png', 'PennPed00048.png', 'PennPed00049.png', 'PennPed00050.png', 'PennPed00051.png', 'PennPed00052.png', 'PennPed00053.png', 'PennPed00054.png', 'PennPed00055.png', 'PennPed00056.png', 'PennPed00057.png', 'PennPed00058.png', 'PennPed00059.png', 'PennPed00060.png', 'PennPed00061.png', 'PennPed00062.png', 'PennPed00063.png', 'PennPed00064.png', 'PennPed00065.png', 'PennPed00066.png', 'PennPed00067.png', 'PennPed00068.png', 'PennPed00069.png', 'PennPed00070.png', 'PennPed00071.png', 'PennPed00072.png', 'PennPed00073.png', 'PennPed00074.png', 'PennPed00075.png', 'PennPed00076.png', 'PennPed00077.png', 'PennPed00078.png', 'PennPed00079.png', 'PennPed00080.png', 'PennPed00081.png', 'PennPed00082.png', 'PennPed00083.png', 'PennPed00084.png', 'PennPed00085.png', 'PennPed00086.png', 'PennPed00087.png', 'PennPed00088.png', 'PennPed00089.png', 'PennPed00090.png', 'PennPed00091.png', 'PennPed00092.png', 'PennPed00093.png', 'PennPed00094.png', 'PennPed00095.png', 'PennPed00096.png']
for i in l:
    f = open(r"Bounded Images//"+i,'wb')
    f.write(request.urlopen('https://www.cis.upenn.edu/~jshi/ped_html/images/'+i[:-4]+"_1.png").read())
    f.close()
    print(i)
