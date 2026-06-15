'''print("Arithmetic Operator")
price_per_book=500
quantity=25
total_price=price_per_book*quantity
average=total_price/quantity
extra_charge=50
final_price=total_price+extra_charge
discount=25
final_price-=discount
remainder=final_price%quantity
floor_division=final_price//7
squared_value=final_price**2

print("Price of one book is: ",price_per_book)
print("Quantity of books: ",quantity)
print("Average: ",average)
print("Extra charge: ",extra_charge)
print("Discount: ",discount)
print("Final price: ",final_price)
print("Remainder: ",remainder)
print("Floor division: ",floor_division)
print("Squared value: ",squared_value)

print("Assignment Operator")
score=100
score+=50
print(score)
score-=20
print(score)
score*=2
print(score)

print("Logical Operator And")
username="sona"
password="SONA"
entered_username=input("Enter the username: ")
entered_password=input("Enter the password: ")
if entered_username==username and entered_password==password:
    print("Login Successful")
else:
    print("Invalid Login")

print("Logical Operator Or")
day=input("Enter a day:")
if day=="Saturday" or day=="Sunday":
    print("Holiday")
else:
    print("Working day")

print("Logical Operator Not")
logged_in=False
if not logged_in:
    print("Please login")
else:
    print("Welcome user")

print("Membership Operator")
movies=["One","Athiradi"]
movie=input("Enter the favorite movie: ")
if movie in movies:
    print("Movie available")
else:
    print("Movie not available")

print("Membership Operator Not")
employees=["V","SK"]
name=input("Enter the employee name: ")
if name not in employees:
    print("Access Denied")
else:
    print("Access Granted")

print("Identity Operator")
value1=100
value2=100
print(value1 is value2)
print(value1==value2)

#Identity Operator in a List
value3=[100,120,130,140,150]
value4=[100,120,130,140,150]
print(value3 is value4)
print(value3==value4)

#Identity Operator in an Index
languages=["Python","Jango","Java"]
selected_language=languages[0]
print(selected_language is languages[0])
print(selected_language == "Python")
print(selected_language is "Python")
print(selected_language is "SQL")
print(selected_language == languages[0])

list1=[10,20,30]
list2=[10,20,30]
print(list1 is list2)
list3=list1
print(list3 is list1)'''

#Bitwise Operator
a=5
b=3
print(bin(a))
print(bin(b))
print(a & b) #and
print(a | b) #or
print(a ^ b) #xor
print(~a) #not
print(a<<1) #left shift
print(a>>1) #right shift