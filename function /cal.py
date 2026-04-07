# a function that that recorgnize the opretoer
def opretoer ( num1 , opretoer , num2):
    opretoer = opretoer .strip()
#erorr handelings
    try:
        # validetion input
        if opretoer == "+":
            add = ( num1 + num2)
            return add 
        elif opretoer == "-":
            less = (num1 - num2)
            return less
        elif opretoer == "*":
            multiply = ( num1 * num2)
            return multiply
        elif opretoer == "/":
            if num2 == 0:
                print( "enter the valid number : ")
            else: 
                devid = ( num1/num2)
                return devid
        else: 
            print( "invalid opretoer  : ")
    except NameError :

        print( "somthings wnat wrong  ! ")
# takeing input from user 
while True: 
    try:  
        num1 = int ( input("etner the number to cal"))
        num2 = int( input( "enter teh seceand number to cal"))
        
    except ValueError:
        print( "ENTER ONLY INT ONLY NUMBER ")
    simble = input( "enter the simble you want to opreate : ")
# function call 
    cal = opretoer ( num1 , simble, num2)
    print(cal)
    break
