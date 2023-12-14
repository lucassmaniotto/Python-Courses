from util.bank_codes import bank_codes

class Account:
    def __init__(self, code, owner, balance, limit):
        self.__code = code
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def deposit(self, value):
        self.__balance += value
        print("\nDeposit of ${} done".format(value))

    def __can_withdraw(self, value_to_withdraw):
        available_value = self.__balance + self.__limit
        return value_to_withdraw <= available_value

    def withdraw(self, value):
        if(not self.__can_withdraw(value)):
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

    @property
    def balance(self):
        return self.__balance
    
    @property
    def owner(self):
        return self.__owner
    
    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return bank_codes["BB"]

print(Account.bank_code())
