def create_account(code, owner, balance, limit):
    account = {"code": code, "owner": owner, "balance": balance, "limit": limit}
    return account

def deposit(account, value):
    account["balance"] += value
    print("Deposit of ${} done".format(value))

def withdraw(account, value):
    if(account["balance"] + account["limit"] < value):
        print("The value {} is greater than the limit".format(value))
        print("Balance: {} Limit: {}".format(account["balance"], account["limit"]))
        return False
    else:
        account["balance"] -= value
        print("Withdraw of ${} done".format(value))
        print("Balance: {} Limit: {}".format(account["balance"], account["limit"]))
        return True

def statement(account):
    print("Hello, {}!".format(account["owner"]))
    print("Code: {} Balance: {} Limit: {}".format(account["code"], account["balance"], account["limit"]))

account = create_account(123, "Nico", 55.0, 1000.0)
deposit(account, 100.0)
withdraw(account, 50.0)
statement(account)
withdraw(account, 10000.0)
withdraw(account, 1000.0)
statement(account)