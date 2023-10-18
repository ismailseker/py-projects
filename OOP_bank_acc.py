class bankAccount:
    def __init__(self,acc_number,acc_holder,acc_balance = 0.0):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.acc_balance = acc_balance

    def deposit(self,amount):
        self.acc_balance += amount

    def withdraw(self,amount):
        if self.acc_balance >= amount:
            self.acc_balance -= amount
        else:
            print("You can't withdraw money. You should deposit.")
    def checkBalance(self):
        return self.acc_balance



account1 = bankAccount('12345','Alex Ferguson',5000.0)
account2 = bankAccount('56789','Jose Mouurinho',2000.0)
account3 = bankAccount('12345','Carlo Ancelotti',4000.0)

account1.withdraw(4000.0)
print(f'Account 1: {account1.acc_balance}')

account2.deposit(8000.0)
print(f'Account 2: {account2.acc_balance}')

print(f'Account 3: {account3.acc_balance}')