# Zero division error

print("Statement 1")
print("Statement 2")
print("Statement 3")
print("Statement 4")
print("Statement 5")
try:
    value1=10
    value2=0
    value3=value1/value2
    print(value3)
except: ZeroDivisionError #if u dont know the class ,simply add "Exception"
print("Denominator cannot be zero")
print("Statement 6")
print("Statement 7")


numerator=int(input("Enter the numerator "))
denominator=int(input("Enter the denominator "))
try:
    quotient=numerator/denominator
except ZeroDivisionError:
    print("Denominator cannot be zero")
else:
    print("Quotient:",quotient)


# type error
try:
    num1=15
    num2="25"
    add=num1+num2
    print(add)
except TypeError:
    print ("cannot add string + int")


# Index error

appointment=[10,11,12,13,14,15]
try:
    print(appointment[8])
except IndexError:
    print("index out of range")



# Key error

book_details={"book_id":2750,
              "book_name":"balarama",
              "bookauthor":"sdfsdf"
             }
try:

    print(book_details["isbn number"])

except KeyError:    
    print("Key not found")



# File not found error

# try:
#     with open("Sample file.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found")


# import error       #wriing by system

# try:
#     from math import square
# except ImportError as e:
#     print(e)


# value error
# try:
#     greet=int("hello")
# except ValueError as e:
#     print(e)


# attribute error

# try:
#     user="Welcome"
#     print(user.add())
# except AttributeError as e:
#     print(e)



# Name error

# try:
#     print(person)
# except NameError as e:
#     print(e)


# multiple exception

# try:
#     print(person)
#     user="Welcome"
    
# except AttributeError as a:
#     print(a)
# except NameError as e:
#     print(e)



# multiple exception another method

# try:
#     print(person)
#     user="Welcome"
    
# except (NameError,AttributeError) as e:
#     print(e)



# final exception

numerator=int(input("Enter the numerator "))
denominator=int(input("Enter the denominator "))
try:
    quotient=numerator/denominator

finally:
    print("Executed normally")


#linear searching
ages=list(map(int,input("Enter the elements to be inserted").split()))
search_element=int(input("Enter the element to search"))
for i in range(len(ages)):
    if ages[i] == search_element:
        print(f"element foundt at position {i+1}")
        break
else:
    print("Element not found")
        