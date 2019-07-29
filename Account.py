def class Account(object):
    def __init__(self, type, owner):
        self.type = type
        self.owner = owner

    def checkBalance():
        print("Here is your account balance ", self.balance)

def class SavingAccount(Account):
    def __init__(self, type, owner, accountNo):
        Account.__init__(self, type, owner)

        def debit(amount):
                try:
                    if self.balance >= amount:
                        debit_Balance = self.balance - amount
                            print("Transaction succesful!")
                            print("Your new balance is ", debit_Balance)

                    else:
                        raise Error
                except Error:
                    print("Insufficient funds!")


        def credit(amount):
            credit_Balance = self.balance + amount
            print("Your new balance is ", credit_Balance)

def class CheckingAccount(Account):
    def __init__(self, type, owner, accountNo):
        Account.__init__(self, type, owner)

                def debit():
                        try:
                            if self.balance >= amount:
                                debit_Balance = self.balance - amount
                                    print("Transaction succesful!")
                                    print("Your new balance is ", debit_Balance)

                            else:
                                raise Error
                        except Error:
                            print("Insufficient funds!")


                def credit():
                    credit_Balance = self.balance + amount
                    print("Your new balance is ", credit_Balance)
