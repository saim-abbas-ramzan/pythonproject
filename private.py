#class student:
#    def __init__(self,name):
#        self.name = name
#s1 = student("saim")
#print(s1.name)
#del s1.name
#print(s1.name)


#private
class account:
    def __init__(self,accno, accpass):
        self.accno = accno
        self.__accpass = accpass
acc1 = account("12345","abcde")
print(acc1.accno)
print(acc1.__accpass)
