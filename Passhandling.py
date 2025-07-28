class InvalidPasswordException(Exception):
    def __init__(self,msg):
        self.msg=msg

password=input("Enter the password: ")
        
passlength=len(password)
try:
        
    if passlength<8:
        raise InvalidPasswordException("Enter a valid 8 charcter password")
    else:
        print("Entered password is perfect")
        
    print("You Password is set succesfully")
except:
    print("enter password is not eligible to set")
    print("Please enter the password more than 8 charcter")
