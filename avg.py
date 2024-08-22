class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
#    @staticmethod
#    def hello():
#       print("hello")
    def getavg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)
s1 = student("saim abbas",[3,3,9])
s1.getavg()
#s1.hello()

# when name change and rerun
#s1.name = "zain abbas"
#s1.getavg()