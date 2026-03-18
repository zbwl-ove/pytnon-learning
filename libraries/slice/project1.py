import sys
# handel some error 
if len ( sys.argv) != 2:
    sys.exit( "give both arguments : ")
#  sliceing the the  part's  
word = (sys.argv [1])
print( word[:2])
word_2 = (sys.argv[1])
print( word[2:])
# reverse printings 
word_3 = ( sys.argv[1])
print ( word[:: -1])
