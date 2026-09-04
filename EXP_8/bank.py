class bank:
    def __init__(self,name,bal,acc_no):
        self.name=name
        self.bal=bal
        self.acc_no=acc_no
        
    def deposit(self,n):
        self.bal+=n
        print(f"amount {n} has been deposited.")
        
    def withdraw(self,n):
        if self.bal>0:
            self.bal-=n
            print(f"amount {n} has been withdrawn.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Balance-->{self.bal}")
        
    def transfer(self,n):
        pass
    
class acc1(bank):
    def __init__(self,n,b,acc):
        super().__init__(n,b,acc)

class acc2(bank):
    def __init__(self,n,b,acc):
        super().__init__(n,b,acc)
obj1=acc1("Customer 1",10000,12345678910)
obj1.check_balance()
obj1.deposit(5000)
obj1.check_balance()

obj2=acc2("Customer 2",500000,9876543210)
obj2.check_balance()
obj2.deposit(50000)
obj2.check_balance()