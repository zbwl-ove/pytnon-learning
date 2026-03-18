# make look's good email :
import sys
# takeings input from the user 
email = input( "enter your email : ")
# slice the email with find

position = email.find("@")
name = email[:position]
print(f"your mame is ", name)
# printing domain name 

domain = email[position+1:]
print("your domain is :", domain)