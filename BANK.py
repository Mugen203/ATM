class Bank:
    code = 123
    address = ' North Street, Box 1219'
    def __init__(self,B_code, B_Address):
        self.B_code = Bank.code
        self.B_Address = Bank.address
    def  __str__(self):
        return f"Bank Code: {self.B_code}\nBank Address:{self.B_Address}"
    def manages(self):
        pass
    def maintains(self):
        pass

print('\n**********************************************************')
aman = Bank(Bank.code,Bank.address)
print(aman)
print('**********************************************************\n')
