lines = int(input("ใส่จำนวนบรรทัดที่ต้องการ : "))
stars = 1
for i in range(lines,0,-1):
    print(i," " * i,"*" * stars)
    stars += 2

