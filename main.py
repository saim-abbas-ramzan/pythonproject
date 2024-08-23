#name = "saim"
#print(name)
#print("hello" + name)

class car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")
class toyotacar(car):
    def __init__(self,name):
        self.name = name
c1 = toyotacar("fortunare")
c2 = toyotacar("4X4")
print(c2.name)
