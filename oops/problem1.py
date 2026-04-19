# ____________CLASS ___________

class student:
# ____________ATTRIBUTES'S _____________________
    name = "rakhi pani"
    marks = 78

# ______________GET GREAD'S FUNCTION  _______________

    def get_gred(self): 
        if self.marks > 90:
            return ( "GREAD A+")
        elif self.marks >60:
            return ("B") 
        elif self.marks <59  :
            return ( "fail") 
        else : 
            return "invlid marks "
        
# ________________DISPLAY PRINT STUDENT'S  ____________________

    def display(self):
        print (self.name , self.marks)
        
# _________________STUDENT CLASS'S OBJECT_______________

love = student ()
love . display ()
print ( love.get_gred ())
