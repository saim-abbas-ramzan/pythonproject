
class information:
    def __init__(self,fulname,fulid):
        self.name = fulname
        self.id = fulid
    def welcome(self):
        print("welcome phython")
m1 = information("saim" ,9)
m1.welcome()
print(m1.name,m1.id)