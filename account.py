class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc
    def debit(self,amount):
        self.balance -=amount
        print("RS.",amount,"was debited")
        print("total balance =",self.getbalance())

    def credit(self,amount):
        self.balance += amount
        print("RS",amount,"was credited")
        print("total balance =", self.getbalance())

    def getbalance(self):
        return self.balance

acc1 = account(10000,1234)
acc1.debit(5000)
acc1.credit(100)