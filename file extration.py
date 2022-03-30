from os import listdir
from os.path import isfile, join
import re

mypath="C://Users//VenkatSaiKota//OneDrive//Desktop//Detect//PennFudanPed//Annotation"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in files:
    n=1
    position=""
    size=0.0
    status=False
    Background_color="White"
    ImageName=i
    Resolution=95
    with open(mypath+"//"+i,'r') as f:
        t=f.read()
        mima_points = re.findall(r"\(Xmin, Ymin\) - \(Xmax, Ymax\) : \(([0-9]+, [0-9]+)\) - \(([0-9]+, [0-9]+)\)", t)
        s=tuple(map(int,re.findall(r"Image size \(X x Y x C\) : ([0-9]+) x ([0-9]+) x [0-9]",t)[0]))
        mid=(s[0]//2,s[1]//2)
        for i in mima_points:
            min_point=tuple(map(int,i[0].split(",")))
            max_point=tuple(map(int,i[1].split(",")))
            a=(max_point[0]-min_point[0])*(max_point[1]-min_point[1])
            A=s[0]*s[1]
            size=a/A
            if(min_point[0]<mid[0] and min_point[1]<mid[1]):
                if(max_point[0]<mid[0] and max_point[1]<mid[1]):
                    position="Top Left"
                elif(max_point[0]>mid[0] and max_point[1]<mid[1]):
                    position="Top"
                elif(max_point[0]<mid[0] and max_point[1]>mid[1]):
                    position="Left"
                elif(max_point[0]>mid[0] and max_point[1]>mid[1]):
                    position="Center"
            elif(min_point[0]>mid[0] and min_point[1]<mid[1]):
                if(max_point[1]>mid[1]):
                    position="Right"
                else:
                    position="Top Right"
            elif(min_point[0]<mid[0] and min_point[1]>mid[1]):
                if(max_point[0]>mid[0]):
                    position="Bottom"
                else:
                    position="Bottom Left"
            else:
                position="Bottom Right"
            n+=1
            l=[ImageName,n,min_point,max_point,position,size,Background_color,Resolution,status]
            #print(",".join(str(it) for it in l))              
            print((max_point[0]-min_point[0],max_point[1]-min_point[1]))
