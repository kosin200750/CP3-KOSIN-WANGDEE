from forex_python.bitcoin import BtcConverter
import datetime,decimal

avg_bitcoin = 0
sum = 0
b = BtcConverter()

usernameinput = input("username : ")
passwordinput = input("password : ")
if usernameinput == "admin" and passwordinput == "1234":
    for i in range(1, 31):
        date_obj = datetime.datetime(2020, 4, i)
        sum += b.get_previous_price('THB', date_obj)

    avg_bitcoin = sum / 30
    txt = "Bitcoin Average in Apirl 2020 is {:.2f}"
    print(txt.format(avg_bitcoin))
else:
    print("Wrong Username or Password!")
