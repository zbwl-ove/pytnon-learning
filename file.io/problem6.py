import sys 
with open ( "p6.txt" , "r") as f :
    content  = f . read ()
    count = content.count ("python")
    if ("python" in content):
        print ("python is present" , count , "time's")
    else :
        print( "python is not present in the content : ")