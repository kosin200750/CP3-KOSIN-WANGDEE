def vatcalculate(totalprice):
    result = totalprice + (totalprice * 0.07)
    return result

print(vatcalculate(int(input("ใส่ราคาสินค้าที่ต้องการ : "))))
