class Vehicle:
    face = ""
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on:Air")

class Car(Vehicle):
    pass

class Pickup(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
pickup1 = Pickup()
pickup1.turnOnAirConditioner()
van1 = Van()
van1.turnOnAirConditioner()
estatecar1 = Estatecar()
estatecar1.turnOnAirConditioner()
