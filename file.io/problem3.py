import sys
# a function that get argv wtih 3 

def arg():
    if len( sys.argv)<3:
        sys.exit( "please enter both argumetn's")
    return sys.argv[1].strip() , sys.argv[2].strip()

# add in the main function

def main ():
    name1 , name2 = arg()
    with open ("names.txt" , "w") as f :
        f.write  (f"{name1 }\n{name2}")
# main functon call and refine for other file 
if __name__=="__main__":
    main()