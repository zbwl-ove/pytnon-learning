import sys
def get_argv():
    if len( sys.argv)<3:
        sys.exit( "please enter both argumetn's")
    return sys.argv[1] , sys.argv[2]
name1 , name2 = get_argv()
with open ("names.txt" , "w") as f :
    content =f.write  (f"{name1 }\n{name2}")
    
            # f.write(f"{name1}\n{name2}")