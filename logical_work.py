# Electricity Bill Calculation

units_consumed=int(input("Enter the unit: "))
if units_consumed<=100:
    total_amount=units_consumed*1
elif units_consumed>100 and units_consumed<=200:
    total_amount=units_consumed*2
else:
    total_amount=units_consumed*3
print("Final Amount: ",total_amount)


# Menu Driven Calculator

number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        result=number1+number2
        print("Addition: ",result)
    elif choice==2:
        result=number1-number2
        print("Subtaction: ",result)
    elif choice==3:
        result=number1*number2
        print("Multiplication: ",result)
    elif choice==4:
        result=number1/number2
        print("Division: ",result)
    else:
        print("Invalid Choice")
        break


# Student Grade System

mark1=float(input("Enter mark of subject 1: "))
mark2=float(input("Enter mark of subject 2: "))
mark3=float(input("Enter mark of subject 3: "))
mark4=float(input("Enter mark of subject 4: "))
mark5=float(input("Enter mark of subject 5: "))
total_mark=mark1+mark2+mark3+mark4+mark5
average_mark=total_mark/5
if average_mark>=90:
    grade="A+"
elif average_mark>=80 and average_mark<90:
    grade="A"
elif average_mark>=75 and average_mark<80:
    grade="B+"
elif average_mark>=70 and average_mark<75:
    grade="B"
elif average_mark>=60 and average_mark<70:
    grade="C+"
elif average_mark>=55 and average_mark<60:
    grade="C"
elif average_mark>=50 and average_mark<55:
    grade="D+"
elif average_mark>=40 and average_mark<50:
    grade="D"
else:
    grade="Fail"
print("Total Mark: ",total_mark)
print("Average Mark: ",average_mark)
print("Grade: ",grade)


# Voting Eligibility Checker

name=input("Enter name: ")
age=int(input("Enter age: "))
if age>=18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")


# Number Guessing Game

attempt=0
secret_number=24
while True:
    number=int(input("Enter number: "))
    attempt+=1
    if number>secret_number:
        print("Guessed number is greater than secret number")
    elif number<secret_number:
        print("Guessed number is less than secret number")
    else:
        print("Guessed number is equal to secret number")
        print("Total Attempts: ",attempt)
    choice=input("Do you want to continue (Yes/No): ").lower()
    if choice=="no":
        break


# Student Attendance Status Checker

student=int(input("Enter number of students: "))
for roll_number in range(1,student+1):
    if roll_number%3==0 and roll_number%5==0:
        print("Low Attendance")
    elif roll_number% 3==0:
        print("Eligible for Exam")
    elif roll_number%5==0:
        print("Attendance Warning")
    else:
        print(roll_number)


# Traffic Signal Simulation

time=int(input("Enter total seconds: "))
for number in range(1,time+1):
    if number%3==0 and number%5==0:
        print("YELLOW")
    elif number%3==0:
        print("RED")
    elif number%5==0:
        print("GREEN")
    else:
        print(number) 


# Online Order Processing System

starting_id=int(input("Enter starting order ID: "))
ending_id=int(input("Enter ending order ID: "))
for order in range(starting_id,ending_id+1):
    if order%3==0 and order%5==0:
        print("Premium Customer Offer")
    elif order%3==0:
        print("Express Delivery")
    elif order%5==0:
        print("Discount Applied")
    else:
        print(order)


# Library Book Categorization

book=int(input("Enter number of books: "))
for book_id in range(1,book+1):
    if book_id%3==0 and book_id%5==0:
        print("Reference Book")
    elif book_id%3==0:
        print("Science Book")
    elif book_id%5==0:
        print("Literature Book")
    else:
        print("General Book")


# Electricity Bill Alert System

starting_range=int(input("Enter starting range: "))
ending_range=int(input("Enter ending range: "))
for customer_id in range(starting_range,ending_range+1):
    if customer_id%3==0 and customer_id%5==0:
        print("Service Suspension Warning")
    elif customer_id%3==0:
        print("High Usage Alert")
    elif customer_id%5==0:
        print("Payment Due")
    else:
        print(customer_id)