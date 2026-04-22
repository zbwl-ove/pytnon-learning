# A banking system 
# a class
class Account :
    
    def __init__(self , name , balance = 0):
        self.name = name
        self.balance = balance

# ==============credit system ====================

    def credit (self , amount ):
        # amount += self.balance i write this ulta 
        self.balance += amount
       
        print (f"balance left{self.show_balance}")

    # ==============balance system================
    
    def  show_balance (self):
        print ( f"\n{self.balance}" , "is your balance")

# ============debit system ===================\
    def debit (self,  amount ):
        int(amount)
        if amount > self.balance:
            print ( " insufficent balance : ")  
        else:
            self.balance-= amount
            print ("you trust me  !")
            print (f"\n {self.show_balance}" , "your balance " )

# 22222222222222222222222 main 222222222222222222222222222

name = input ("your name !")
love = Account(name)
    # ----------------- menu--------------
while True:
    print ( '''
        1 for balance
        2 for withdrowel
        3 for depsit
        ''')
    # -------------------balence -------------------

    choice = int (input ("no !"))
    if choice == 1 :
        love.show_balance()

        print(love.show_balance)

    # =========================debit=====================

    elif choice == 2 : 
        print ("redy for withdrowl ; ")
        while True:
            try:
                cash = int (input ("enter hear amount"))
                break
            except ValueError : 
                print ("ops number only ! ")
        love.debit(cash)
        print ("withdrowl sucssesfully :" , cash , "repees ; ")
        print (love.show_balance)

        # ===============credt=======================

    elif choice == 3:
        while True:
            try:
                cash = int (input ("enter hear amount"))
                break
            except ValueError : 
                print ("ops number only ! ")
            love.credit(cash) 
            print (f"hogeya : {cash} itne add  " )
            print ( love.show_balance)
    op = input ("press enter to continu or press exit ")
    if op == "exit":
        break
    else :
        print (f"thanks{name}")
