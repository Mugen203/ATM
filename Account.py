#Account class to hold data on all the accounts created by the bank
class Account(object):
    def __init__(self, type, owner, balance, accountNo):
        self.type = type
        self.owner = owner
        self.balance = balance
        self.accountNo = accountNo

    #Returns data on the balance remaining in the bank account
    def check_balance(self.balance):
        return balance

    #Debits the account
    def debit(amount):
        try:
            if self.balance >= amount:
                debit_Balance = self.balance - amount
                return debit_Balance

            else:
                raise Error

        except Error:
            print("Insufficient funds!")

    #Credits the account
    def credit(amount):
        credit_Balance = self.balance + amount
        print("Your new balance is ", credit_Balance)


class SavingAccount(Account):
    def __init__(self, type, owner, balance, accountNo):
        Account.__init__(self, type, owner, balance, accountNo)

class CheckingAccount(Account):
    def __init__(self, type, owner, balance, accountNo):
        Account.__init__(self, type, owner)
