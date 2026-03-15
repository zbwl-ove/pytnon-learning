import sys
# handeling some erorr

if len  ( sys . argv) != 3 :
    sys.exit( "enter two argumnt  name and age ")
# gitting safe code and print  

print( "your name is ", sys.argv[1])
print( "age " , sys. argv[2])