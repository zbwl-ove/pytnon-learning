# a project that a working calculetor from command line argumnts 
import sys 
# handel some errors 
if len ( sys. argv) != 4 :
    sys.exit( "use valu like nubmer opreter nubmer ")
# add logic for opretors
a = int ( sys.argv[1])
b = int( sys.argv[3])
op = ( sys.argv[2])
# add oprater logic
if op == "+":
    print( a+b)
elif op == "-":
    print( a - b)
    
elif op == "*":
    print( a * b)
# specila  0 handelings with opterter
elif op == "/":
    try: 
        print( a/b)
    except ZeroDivisionError:
        print( "can't / by zero :")
else : 
    print( " unknown opteter ")

    