class Atm(object):
    def __init__(self , cardNumber , pinNumber ):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        

    def CashWithdrawl(self):
        print("Cash Withdrawed")
    
    def SelfEnquiry(self):
        print("Self Enquiry Desktop Opened")
    
    def CashGiven(self):
        print("Cah Given")

soham = Atm("9765 3002 1211 2008" , "3027")
print(soham.cardNumber)
print(soham.pinNumber)


soham.SelfEnquiry()
soham.CashWithdrawl()
soham.CashGiven()

Mom = Atm("5742 3097 1973 0306 " , "2873")
print(Mom.cardNumber)
print(Mom.pinNumber)

Mom.SelfEnquiry()
Mom.CashWithdrawl()
Mom.CashGiven()



