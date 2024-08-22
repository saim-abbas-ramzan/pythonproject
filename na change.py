class person:
    name = "zain abbas"
    def changename(self, name):
        self.name = name
p1 = person()
p1.changename("saim abbas")
print(p1.name)
print(person.name)