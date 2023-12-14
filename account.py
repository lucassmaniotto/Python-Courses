class Account:
    def __init__(self, code, owner, balance, limit):
        self.code = code
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def deposit(self, value):
        self.balance += value
        print("Deposit of ${} done".format(value))

    def withdraw(self, value):
        if(self.balance + self.limit < value):
            print("The value {} is greater than the limit".format(value))
            print("Balance: {} Limit: {}".format(self.balance, self.limit))
            return False
        else:
            self.balance -= value
            print("Withdraw of ${} done".format(value))
            print("Balance: {} Limit: {}".format(self.balance, self.limit))
            return True
        
    def statement(self):
        print("Hello, {}!".format(self.owner))
        print("Code: {} Balance: {} Limit: {}".format(self.code, self.balance, self.limit))

account = Account(123, "Nico", 55.0, 1000.0)
account.deposit(100.0)
account.withdraw(50.0)
account.statement()
account.withdraw(10000.0)
account.withdraw(1000.0)
account.statement()