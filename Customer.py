class Customer(object):

    def __init__(self, customer_id, Fname, Lname , adderss, dob, acc_no):
        self.customer_id = customer_id
        self.Fname = Fname
        self.Lname = Lname
        self.adderss = adderss
        self.dob = dob
        self.acc_no = acc_no


    def Customer_info(self):
        #***THE IF STATEMENT COMMENT*****i  did this incase we want the customer to pass in customer ID before 
        #.... he or she can ass his or her information so we can delete it
        '''pin = int(input("Enter Your Pin Number: "))
        if pin != self.customer_id:
            print("Invalid pin kindly check and enter again")
        else:'''
        print("************ CUSTOMER INFORMATION ****************")

        print("Customer ID: {}\n First Name: {}\n Last Name: {}\n Address: {}\n Date of Birth: {}\n Account Number: {}".format(self.customer_id,self.Fname,self.Lname,self.adderss,self.dob,self.acc_no))

    def owns(self,Account):
        pass


C1 = Customer(1001,"Frank","Mensah","Box 15", "July 16 1887", 10001)
C2 = Customer(1002,"Owusu","Fred","Box 15", "July 16 1887", 10001)
C2.Customer_info()
