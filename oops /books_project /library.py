import sys
class library :

# take file name for by defult pick 

    def __init__(self  ,file_name = "store_books.txt" ):
        self.file_name = file_name
# add books 


    def add_books(self):
        try:
            authoer = input ("Enter  Auther Name ") .strip()
            book_name = input ("Enter book name").strip()
            pcs = int (input("pcs ! ") )
            
            with open (self.file_name , "a") as f :
                 f.write(f"{authoer} , {book_name} ,{pcs} \n")
                 print ("book added :")
        except FileNotFoundError  as e :
            print (e)
        except Exception as e :
            print (e)
        except ValueError :
            print ("enter int only in pcs !")
    def remove_book(self ,):
        
        try :
            book = input ("enter the book you wan't to remove :")
            with open(self.file_name , "r")as f :
                line = f.readlines()
            with open (self.file_name, "w") as f :
                for line in line :

            
love = library ()
love.add_books()
