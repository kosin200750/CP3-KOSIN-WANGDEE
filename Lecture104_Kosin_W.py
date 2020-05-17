class Customer:
    fname = ""
    lname = ""
    age = 0
    def addCart(self):
        print("add product to",self.fname,self.lname,self.age," 's cart")

customer1 = Customer()
customer1.fname = "Kosin"
customer1.lname = "Wangdee"
customer1.age = 46
customer1.addCart()
customer2 = Customer()
customer2.fname = "Kwanta"
customer2.lname = "Riewphaiboon"
customer2.age = 45
customer2.addCart()
customer3 = Customer()
customer3.fname = "Kiti"
customer3.lname = "Singhapat"
customer3.age = 58
customer3.addCart()
customer4 = Customer()
customer4.fname = "Thanachai"
customer4.lname = "Boonchum"
customer4.age = 36
customer4.addCart()
