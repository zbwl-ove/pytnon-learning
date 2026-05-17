class add_books :
    def  __init__(self , filename):

        self.filename = filename
        
    #  add books 

    def add_books (self):
        try :
            book_name = input ( "enter book name :").strip()
            pcs  = int(input("enter quntity : ")).strip()
            authoer = input ("enter auther name :").strip()
            with open (self.filename, "a") as f :
                f . write (f"book name = {book_name}\n pcs = {pcs} \n auther - {authoer}")
                print ("book add sucssesfully : ")
        except ValueError : 
            print ("enter in pcs only number : ")
        except FileNotFoundError : 
            print ("data.txt file dose not exits : ")
        except Exception as e :
            print ( e )
# ________________ remove books ________________
class remove_book(add_books) :
    def books(self):
        try: 
            book = input ("enter book you wan remove ; ").lower().strip()
            new_line = []
            
            with open (self.filename , "r" )as f :
                lines = f.readlines ()
                for line in lines :
                    if line .split(",")[0].lower().strip():
                        if line != book :
                            new_line.append(line)
                        # chake is that name is exits  and add all into a new list

# -----------------------------------------------------------------

        # print the new data ill get thorugh out the new file 
            with open(self.filename , "w") as f :
                f.writelines(new_line)
                print ("book remove sucssefully : ")
                print (new_line)

                    

        except FileNotFoundError :
            print ("file not exiist : ")
        except Exception as e :
            print(e)
                    

love = remove_book("data.txt")
love .books()





          