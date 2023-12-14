class Account:
    def __init__(self, code, owner, balance, limit):
        self.__code = code
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def deposit(self, value):
        self.__balance += value
        print("\nDeposit of ${} done".format(value))

    def withdraw(self, value):
        if(self.__balance + self.__limit < value):
            print("\nThe value {} is greater than the limit".format(value))
            print("Balance: {} Limit: {}".format(self.__balance, self.__limit))
            return False
        else:
            self.__balance -= value
            print("\nWithdraw of ${} done".format(value))
            print("Balance: {} Limit: {}".format(self.__balance, self.__limit))
            return True
        
    def statement(self):
        print("\nHello, {}!".format(self.__owner))
        print("Code: {} Balance: {} Limit: {}".format(self.__code, self.__balance, self.__limit))

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)
        print("\nTransfer of ${} done from {} to {}".format(value, self.__owner, destiny.__owner))

account = Account(123, "Nico", 55.0, 1000.0)
account2 = Account(321, "Marco", 100.0, 1000.0)
account.statement()
account2.statement()
account.transfer(10.0, account2)
account.statement()
account2.statement()