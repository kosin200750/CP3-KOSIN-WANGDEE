NameList=[]
MenuDict={"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวหมูแดง":40,"ไอศครีม":20,"ซุปข้าวโพด":30}
def showbill():
    tot = 0
    print("--------MAX FOOD--------")
    for i in range(len(NameList)):
        print(NameList[i])
        tot += NameList[i][1]
    print("ราคารวมทั้งหมด %d บาท" %(tot))

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    NameList.append([menuName,MenuDict[menuName]])

showbill()
