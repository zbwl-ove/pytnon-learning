# password masker 
import sys
# checkeing some error
if len(sys.argv)!= 2:
    sys.exit(" need two arguments : ")
# limit the visible  part of the password  
password = sys.argv[1]
print( password[:3] ,end="")
# Now printing the rest with "*"
mask = "*"* max(0, len ( password)- 3)
print( mask)
