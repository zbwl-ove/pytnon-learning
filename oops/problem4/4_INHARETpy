# A smart banking system 
class Account :
    def __init__(self ,balance= 0 ):
        self . balance =balance
        # -----------show balance----------------------

    def show_balance (self):
        print (self.balance , " balance")

    # ---------------deposti--------------

    def deposit (self , amount):
            self.balance += amount 
            print (f"{amount} credited sucssefully : ")
            self.show_balance
            return self.balance
    

    #____________withdrawll _______________

    def withdrawl(self , amount):
            
                if amount > self.balance : 
                    print ("don't have sufficeant money")
                elif amount < 0 :
                    print ("negetive amount na na na : ")
                else :
                     self.balance -= amount
                     self.show_balance()
                     return self.balance
                
# -----------------create saving Account--------------
class SavingAccount(Account):

    # ------------intrest rate-----------------
    
    def cal_intrest (self ,rate , time):
         intrest = ( self.balance * rate* time) /100
         self.balance += intrest
         print ("intrest is " , intrest , )
         print ( "balance is " , self.balance)
         
         
         
# -----------carrent ac----------------
class CarentAccount(SavingAccount):
     def withdrawl(self, amount):
        if amount > 50000 : 
               print ( "you can't withdrow 1lakh at a time only 50k is allowed : ")
        else:   
             self.balance -= amount
             self.show_balance()
             print ( "withrowl succsesfully")
            

# =================class call =================
maya =Account()
maya.show_balance()
maya.deposit (1000)
maya.withdrawl(100)
maya = SavingAccount(maya.balance)
maya.cal_intrest(3 , 10 )
maya. withdrawl (80)    

