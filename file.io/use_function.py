# for countion car
def count_car( content):
    return( len (content))
# for counting word 
def count_word (content):
    return ( len( content . split ()))
# for couting line's
def count_line(content):
    with open ( "data.txt")as f :
        content = f. readlines()
        return  ( len(content))
# making a unvarsall function 
def main ():
    with open ( "data.txt")as f :
        content = f . read()
# function call 
    print( count_car (content) , "this is your total  car ")
    print( count_line ( content) , "this is you'r total of  line ")
    print( count_word (content), "this is your total of word  ")
if __name__== "__main__":
    main()