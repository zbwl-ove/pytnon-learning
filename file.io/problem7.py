#  A SMALL SCHOOL SYSTEM 


#____________ STUDENT ADD FUNCTION _________

def add_student ():
    name= input("enter your name ")
    try :
        marks = int (input ("enter your marks hear : "))
    except ValueError : 
        print ( "please enter valied marks  : ")
        return
    if marks > 90 :
       status =  "GRADE A+"
    elif marks > 60 :
        status =  "GRADE B "
    else : 
        status = "fail "
    with open ("student.txt" , "a") as f :
        f.write (f"{name} , {marks} , {status} \n")
        print("student add sucssesfully :")
    
# ______________________STUDENT STATUS SHOW __________________

def status_show ():
    student = input ( "enter your name   ; ")
    found = False
         
    with open ("student.txt" , "r") as f :
        for line in f :
            name , marks , status = line .strip () . split(" , ")
            if student . lower () ==  name . lower():
                print  (f"{name} , {status}")
                found = True
    
    if not found :
        print ("name not found : ")


 # __________________MAIN ____________________

def main ():
    while True:
        print ( "add or show or exit ")
        action = input ("enter hear : ") . lower ()
        
        if action == "add":
            add_student () 
        elif action == "show":
            status_show()
        elif action =="exit": 
            print  ( "sucssesfully exit  : ")
            break
        else : 
            print ( "invalid action ")

# ____________FUNCTION CALL _______________

if __name__=="__main__":
    main ()