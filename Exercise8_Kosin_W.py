usernameinput = input("username : ")
passwordinput = input("password : ")
if usernameinput == "admin" and passwordinput == "1234":

    item = ""
    print("------------MAX SHOP------------")
    print("-------เลือกรายการสินค้าที่ต้องการ------")
    print("1.น้ำดื่ม ขวดละ 10 บาท")
    print("2.แล็คตาซอย กล่องละ 15 บาท")
    print("3.MAMA ซองละ 10 บาท")
    print("4.เลย์มันฝรั่ง ห่อละ 35 บาท")
    print("5.ชาเขียว แก้วละ 25 บาท")
    print("6.ชาดำเย็น แก้วละ 15 บาท")
    print("7.ชามะนาว แก้วละ 20 บาท")
    print("8.ถั่วกรอบแก้ว ซองละ 10 บาท")
    print("9.น้ำลิ้นจี่ แก้วละ 10 บาท")
    print("10.น้ำลำไย แก้วละ 10 บาท")

    choice=int(input("Please Selected Choice =>"))
    if choice == 1:
        quan = int(input("ใส่จำนวนที่ต้องการ"))
        unitprice = 10
        item = "น้ำดื่ม"
    elif choice == 2:
        quan = int(input("ใส่จำนวนที่ต้องการ"))
        unitprice = 15
        item = "แล็คตาซอย"
    elif choice == 3:
        quan = int(input("ใส่จำนวนที่ต้องการ"))
        unitprice = 10
        item = "MAMA"
    elif choice == 4:
        quan = int(input("ใส่จำนวนที่ต้องการ"))
        unitprice = 35
        item = "เลย์มันฝรั่ง"
    elif choice == 5:
        quan = int(input("ใส่จำนวนที่ต้องการ"))
        unitprice = 25
        item = "ชาเขียว"
    elif choice == 6:
        quan = int(input("ใส่จำนวนที่ต้องการ"))
        unitprice = 15
        item = "ชาดำเย็น"
    elif choice == 7:
        quan = int(input("ใส่จำนวนที่ต้องการ"))
        unitprice = 20
        item = "ชามะนาว"
    elif choice == 8:
        quan = int(input("ใส่จำนวนที่ต้องการ"))
        unitprice = 10
        item = "ถั่วกรอบแก้ว"
    elif choice == 9:
        quan = int(input("ใส่จำนวนที่ต้องการ"))
        unitprice = 10
        item = "น้ำลิ้นจี่"
    elif choice == 10:
        quan = int(input("ใส่จำนวนที่ต้องการ"))
        unitprice = 10
        item = "น้ำลำไย"

    if item == "":
        print("ไม่มีรายการที่ต้องการ")
    else:
        total = unitprice * quan
        print("คุณได้ซื้อ",item,"จำนวน",quan,"หน่วยๆ ละ",unitprice,"บาท รวมเป็นเงิน",total,"บาท")
else:
    print("Wrong Username or Password")
