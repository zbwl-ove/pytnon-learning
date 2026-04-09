import random

# a rendom number provider function 

def game ():
    print( "your now playing this game ")
    highe_scoer = random.randint(1, 100)
    return highe_scoer

# read content of scoer.txt

with open ("ex.txt")as f :
    content = f. read ()

# taking a highe_scoer

highe_scoer = game()  
print( "your score is " , highe_scoer)   

# a condition that cheake won or loose 
if highe_scoer > int ( content ):
    with open ( "ex.txt"  , "w") as f :
        f . write (str(highe_scoer))
    print( "your are hero ")
elif highe_scoer == "":
    content == 0
    print( "your are hero ")    
else : 
    print( "you are not  a hero ")