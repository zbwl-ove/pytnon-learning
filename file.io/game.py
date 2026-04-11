import random

# ENTER TO GAME 
    
def game ():
    print("NOW YOUR PLAYING THIS GAME :" )
    return random.randint( 1 , 100 )
score = game ()
print(  "your scoer is : ",  score)

# READE FILE SAFFLI 

try:
    with open ("ex.txt") as f :
         content = f . read ()
         if content == "":
             content = 0
         else :
             content = int(content)
        
except FileNotFoundError:
    content = 0

# # GAME PLAY
if score > content : 
    with open ("ex.txt"  , "w") as f :
        f . write (str(score ))
        print( "your a herroo  :")
else:
    print( "you looose the game :")

