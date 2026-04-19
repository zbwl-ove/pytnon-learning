import  sys
from random import randint
class bankaccount :
   
#  _________INCENTENCE_____________ 
    def __init__(self):
        pass
    
#----------------create costemer  ----------------
    @staticmethod
    def add_costemer ():
        name = input ("enter your name  : ") 
        
        with open ("costmer.txt" , "r") as f : #cheack costmer exist 
            content = f . read ()
            if name in content :
                print ( "sorry your exist")
                return
        balance = int (input ("enter amount : "))
        write_file ("costmer.txt"  , "a"  , name , balance)

                
# ---------------------bank deposit logic----------------------

    def deposit ():
        try :
            amount = int ( input ( "enter the deposit amount  : "))
        except Exception as e :
            print ( "erorr happend " , e)
        with open ( "costmer.txt" , "r") as f : 
            content = f . read ()
            if content 

# ------------ file write function ----------------
def write_file(filename , mode , name= None , balance= None ): # remember this order 
    try:
        with open (filename , mode) as f : # take file and mode or start 
            if name and balance  :
                f . write (f"{name},{balance} \n"  ) # passing valu as one str  ""
            
            elif name :
                f . write (f"{name}\n")
            elif balance :
                f . write (f"{balance}\n")
            else:
                print ("only take name and balance  ; ")
    except Exception as e :
        print  ( "erorr happend", e)



# -------------this include a **keargs and *args so for now ill pass-------------------

#
# def file ( *args , **data):
#     try : 
#         with open ( str(data) ,  str(data) , )as f :
#             content = f . write (data)

#     except Exception as e : 
#         print ( "erorr happend "  , e)    
# name = "rajesh"
# data = file("student.txt" , "w"  , name )
