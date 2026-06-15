#Password Strength Checker

password=input("Enter a password: ")
def secure():
    def strong():
        if len(password)>=8:
            return "Strong Password"
        elif len(password)>=6:
            return "Medium Password"
        else:
            return "Weak Password"
    print(strong())
secure()
    
