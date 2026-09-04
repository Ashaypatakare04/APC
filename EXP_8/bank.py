class bank:
    def __init__(self,name,acc_no):
        self.name=name
        self.bal=0
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
    def __init__(self,n,acc):
        super().__init__(n,acc)

class acc2(bank):
    def __init__(self,n,acc):
        super().__init__(n,acc)
        
obj1=acc1("Customer 1",12345678910)
obj1.deposit(5000)
obj1.check_balance()
obj1.withdraw(1000)
obj1.check_balance()

obj2=acc2("Customer 2",9876543210)
obj2.deposit(50000)
obj2.check_balance()
obj1.withdraw(1000)
obj2.check_balance()
