class person:
    name = "saim"
    def __hello(self):
        print("hello person!")
    def welcome(self):
        self.__hello()
p1 = person()
print(p1.name)
print(p1.welcome())