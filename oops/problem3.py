# a banking logic 
class Account:
    def __init__(self ,  debit , credit ,  ):
        self.debit= debit
        self.credit = credit
        # self.balence = balence
# =-------------------debit logic ----------------
    def debit (self):
        if self.balence > self.debit : # withdrow < balance 
            self.balence-= self.debit # from blaence make less debit amount 
            print ( " transection sucssecfully ")
            print (self.balence)
            return self.balence
        else :
            "you dont have that amount in you bank account ; "
# ------------------credit--------------------------------
    def credit(self):
        amount =  int (input ( "enter your withdrow amount : "))
        amount += self.balence # Add credit amount 
        print ( "deposit sucssecfully ; ")
        print ( self.balence)
        return self.balence
# ------------------balance------------------
    # def balence (self):
    #     print (self.balence)
    #     return self.balence #return reamaing balnce 

costmer = Account 
costmer (1000 , 53 )
print (costmer)
