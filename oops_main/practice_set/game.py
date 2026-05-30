

# import random
# n = random.randint(1, 50) # this is gives a random numbe
# a = -1
# guesses = 1
# while (n!=a):
#     try :
#         a = int(input("guesss the number : "))
#         if a > n:
#             print( "loweer number : ")
#             guesses +=1
#         elif a < n :
#             print( "higher number  ; ")
#             guesses +=1
#     except ValueError : 
#         print ("enter int only ;  ")
# print (f"you gussed right in {guesses} guesses  ")

# match   

# def status_code (status):
#     match status :
#         case 403 :
#             print ("its a htttps protocale : ")
#         case 80 :
#             print( "its http protocale ")
#         case _:
#             print ("rendom protocles ; ")
# status_code (403)


# list = [1,2,3,4,5,6,7,8]
# for i , item in enumerate(list):
#     if i == 0 or i == 4 or i == 7:
#         print ( item )
n = 3434379323
table = [n*i for i in range (1 , 11)]
print (table)