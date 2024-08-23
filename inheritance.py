class car:
    colour = "black"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car sotped..")
class toyota(car):
    def __init__(self,brand):
        self.brand = brand
car1 = toyota("fortuner")
car2 = toyota("BMW")
print(car1.colour)
print(car2.brand)

#multi level
class car:
    colour = "blue"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car sotped..")
class toyota(car):
    def __init__(self,brand):
        self.brand = brand
class fortuner(toyota):
    def __init__(self,type):
        self.type = type
car1 = fortuner("diesel")
print(car1.type)

#multiple level
class a:
    vara = "welcome to class is a"
class b:
    varb = "welcome to class is b"
class c(a, b):
    varc = "welcome to class is c"
c1 = c()
print(c1.vara)
print(c1.varb)
print(c1.varc)
