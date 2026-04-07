
# printing the totall car of data.txt
with open ( "data.txt" ,'r') as f : 
    content = f.read ()
    print( len( content) ,end="")
    print( "  , car's")
# printing totall of word's in data.txt   
with open ( "data.txt", "r") as f : 
    content = f.read () . split ()
    print( len( content) ,end="")
    print( "  , word's")
# printting the total line of data.txt
with open ( "data.txt",  "r" ) as f : 
    content = f.readlines()
    print( len (content))
    