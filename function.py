'''#SYNTAX OF FUNCTION
def function_name(parameters):
    code to be executed


def greeting(user_name,age):
    print(f"Welcome {user_name} you are {age} old.")
user_name=input("Enter Name: ")
age=int(input("Enter age: "))
greeting(user_name,age)


def addition(num1,num2):
    return num1+num2
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
print(addition(num1,num2))
#result=addition(num1,num2)
#print(result)
#RETURN FUNCTION IS USED TO SEND A VALUE BACK TO THE CALLER


def welcome():
    print("Welcome")
welcome()


#POSITIONAL ARGUEMENTS--> POSITION MATTERS
def book_ticket(movie_name,customer_name,seats,ticket_price):
    total=seats*ticket_price
    return f"{customer_name} booked {seats} tickets for {movie_name}. Total Amount: {seats}"
print(book_ticket("Vazhaa","Anu",5,200))
#print(book_ticket(3,400,"Joel","Teddy"))


#KEYWORD ARGUEMENTS--> KEY VALUE PAIRS
print("\nkeyword arguements")
def customer_details(customer_name,age,city):
    print(f"Customer Name: {customer_name}")
    print(f"Customer Age: {age}")
    print(f"City: {city}")
customer_details(age=20,city="Kollam",customer_name="Sona")


#DEFAULT ARGUEMENTS
print("\ndefault arguements")
def booking_status(customer_name,status="Confirmed",screen="Screen1"):
    print(f"{customer_name}'s booking status: {status}")
    print(f"Screen allocated: {screen}")
booking_status("Sona")
booking_status("Sumin","Pending")
booking_status("Parvathy","Pending","Screen3")


#MULTIPLE ARGUEMENTS
def calculate_bill(*ticket_prices):
    print(f"Ticket Prices: {ticket_prices}")
    print(f"Total Bill: {sum(ticket_prices)}")
calculate_bill(150,160,200,250)


#MULTIPLE KEYWORD ARGUEMENTS
def passenger_info(**details):
    print("Customer Information: ")
    for key,value in details.items():
        print(f"{key}: {value}")

passenger_info(
    customer_name="Sona",
    seats=2,
    destination="Korea",
    payment_status="Pending"



#BUILT-IN FUNCTIONS
print(len("Sumin"))
print(sum([2,5]))
print(max([10,12,14,16]))
print(min([1,2,3,4]))
print(sorted([9,4,7,3,6]))
print(sorted([9,4,7,3,6],reverse=True))


languages=["Malayalam","English","Hindi","Korea"]
print(sorted(languages))
print(sorted(languages,reverse=True))
print(sorted(languages,key=len))
print(sorted(languages,key=len,reverse=True))


#Enumerate working in a function


#LEGB RULE-->LOCAL ENCLOSING GLOBAL BUILT-IN
#LOCAL VARIABLE

def student_details():
    name="Sona"#LOCAL VARIABLE
    print("Student Name: ",name)
student_details()


#GLOBAL VARIABLE

college_name="Travancore Engineering College Oyoor"
def display():
    print("College Name: ",college_name)
display()


#ENCLOSING VARIABLE

def department():
    department_name="Computer Science"
    def student():
        print("Department: ",department_name)
    student()
department()


#BILLING SYSTEM

tax=50#GLOBAL VARIABLE
def shopping():
    discount=150
    def bill():
        amount=1800
        total_amount=amount-discount+tax
        print("Amount: ",amount)
        print("Discount: ",discount)
        print("Tax: ",tax)
        print("Total Amount: ",total_amount)
    bill()
shopping()


#FACTORIAL OF A NUMBER

def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))

#WORKING

5*fact(4)
4*fact(3)
3*fact(2)
2*fact(1)

1*2=2 fact(2)=2
3*fact(2)=3*2=6
4*fact(3)=4*6=24
5*fact(4)=5*24=120

fact(5)
=5*fact(4)
=5*(4*fact(3))
=5*(4*(3*fact(2)))
=5*(4*(3*(2*fact(1))))


#FACTORIAL DIRECT WAY

number=int(input("Enter a number: "))
factorial=1
for num in range(1,num+1):
    factorial*=num
print(num)


#LAMBDA FUNCTION

def add(a,b):
    return a+b 
print(add(3,4))

#SYNTAX OF LAMBDA FUNTION
lambda arguements:expression

add=lambda a,b:a+b 
print(add(5,4))


#SQUARE OF A NUMBER

square=lambda x:x*x
print(square(5))


#LARGEST OF TWO NUMBERS

largest=lambda a,b: a if a>b else b 
print(largest(2,7))'''