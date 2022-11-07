#from facerec import Image_Face_Recognition_System as fr
#fr()

with open('attendance.csv', 'r+') as attendance:
    MyDatalist =  attendance.readlines()
    NameList = []
    NameList.append(MyDatalist[2])
    MyName = NameList[0]
    MyName = MyName.replace("'", '')
    MyName = MyName.split(",")
    MyName = MyName[0]
    print(MyName)

#python testFR.py