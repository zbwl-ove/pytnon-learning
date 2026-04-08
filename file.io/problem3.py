import sys
def get_argv():
    if len( sys.argv)<3:
        sys.exit( "please enter both argumetn's")
    return sys.argv[1].strip() , sys.argv[2].strip()
def main ():
    
    name1 , name2 = get_argv()
    with open ("names.txt" , "w") as f :
        f.write  (f"{name1 }\n{name2}")
if __name__=="__main__":
    main()