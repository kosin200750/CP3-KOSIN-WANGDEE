NameList=[]

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
    else:
        menuPrice = int(input("Price : "))
    NameList.append([menuName,menuPrice])

showbill()
