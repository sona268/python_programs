'''class CustomException(Exception):
    pass
def check_number(num):
    if num<0:
        raise CustomException("Not allowed negative numbers")
    return num
try:
    result=check_number(2)
    print(result)
except CustomException as e:
    print(e)
'''

# name too short error

class NameTooShortError(Exception):
    pass
name=input("Enter name: ")
try:
    if len(name)<5:
        raise NameTooShortError("Name is too short")
    else:
        print("Welcome ",name)
except NameTooShortError as n:
    print(n)
finally:
    print("Close")