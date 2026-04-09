with open ("name.txt" ,"a") as f : 
    while True:
        names = input("enter name's  or tyip exit : ")
        if names == "exit":
            break
        else:
            content = f .write (names)
            print(f"sucsessfully added" , names )
