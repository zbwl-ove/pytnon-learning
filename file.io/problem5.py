# TAKE INPUT AS APPEND MODE SO OLD DATE NOT CHANGE  
with open ("name.txt" ,"a") as f :
    while True:
        names =  input("enter name's  or tyip exit : ")
# TAKING INPUT AS LOWER 
        if names.lower() == "exit":
            break
# BREAK PROGRAM BY TYIP EXIT
        else:
            # TAKE NEXT LINE BY \N WITH  "" 
            f .write (names  + "\n" )
            print(f"sucsessfully added" , names )
