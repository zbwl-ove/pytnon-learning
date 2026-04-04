with open ( "info.txt", "r")as f :
    for i , line  in enumerate(f  , start=1):
        print( f"NO{i}, {line}")