class account(object):
    def __init__(self, type, owner,account_number,pin,balance):
        self.type = type
        self.owner = owner
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def debit(self,amount):
        deposit_balance = self.balance - amount
        return deposit_balance

    def credit(self,amount):
        credit_balance = self.balance + amount
        return credit_balance
    #End of the class.