NameList=[]
PriceList=[]

def showbill():
    tot = 0
    print("--------MAX FOOD--------")
    for i in range(len(NameList)):
        print(NameList[i],PriceList[i])
        tot += PriceList[i]
    print("ราคารวมทั้งหมด %d บาท" %(tot))

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
    NameList.append(menuName)
    PriceList.append(menuPrice)

showbill()
