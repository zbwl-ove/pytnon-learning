class Account :
    Branch = "khallikot"

    def __init__(self ,balance = 0):
        self.balance= balance

    #    ------------ # credit logic ------------
    def credit (self):
            try:
                credit_amount = int( input ( "enter your credit amount"))
            except ValueError :
                print ( " enter only int valu ; ")
            self.balance += credit_amount
            print ( self.balance)
            return self.balance
        # ----------------debit logic- -----------------
    def debit (self):
            try :
                debit_amount = int (input("enter debit amount : "))
            except Exception as e :
                print ("erorr happend "  , e)
            if debit_amount > self.balance :
                return "your balance is low "
            elif debit_amount < self.balance :
                self.balance -= debit_amount
                print ( "your balance is " , self.balance )
                return self.balance
            else :
                return "invalid amount"
maya= Account ()
maya.debit ()
maya.balance()
maya.credit()

# this code was worng and i ll create onther practice file 
