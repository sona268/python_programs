# PRIME NUMBER USING BOOLEAN
'''
number=int(input("Enter a number: "))
if number<=1:
    print("Not a prime number")
else:
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
            break
    if is_prime:
        print("Is a prime number")
    else:
        print("Not a prime number")
'''

# PRIME NUMBER USING COUNT

# PRIME NUMBER USING FLOOR DIVISION

# FIBONACCI SERIES
'''
n=int(input("Enter the number of items: "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b 
    a=b
    b=c 
'''

# PALINDROME NUMBER
'''
number=int(input("Enter the number: "))
digit=number
reverse=0
while number>0:
    remainder=number%10
    reverse=reverse*10+remainder
    number//=10
if digit==reverse:
    print("The number is a palindrome number")
else:
    print("The number is not a palindrome number")
'''

# COUNT THE NUMBER OF DIGITS
'''
number=int(input("Enter the number: "))
count=0
temp=abs(number) # abs --> ABSOLUTE VALUE
if temp==0:
    count=1
else:
    while temp>0:
        count+=1
        temp=temp//10
print("Number of digits ",count)
'''

# SUM OF DIGITS
'''
number=int(input("Enter the number: "))
sum_digit=0
temp=abs(number)
while temp>0:
    digit=temp%10
    sum_digit+=digit
    temp=temp//10
print("Sum of digits is ",sum_digit)
'''

# PRODUCT OF DIGITS
'''
number=int(input("Enter the number: "))
product=1
temp=abs(number)
while temp>0:
    digit=temp%10
    product*=digit
    temp=temp//10
print("Product of digits is ",product)
'''

# ATM
'''
corret_pin=1234
balance=50000
attempts=0
while attempts<=3:
    pin=int(input("Enter a pin: "))
    if pin==corret_pin:
        print("Login Successful")
        while True:
            print("\n1. Balance Check")
            print("2. Withdrawal")
            print("3. Deposit")
            print("4. Exit")
            choice=int(input("Enter the choice: "))
            if choice==1:
                print("Balance: ",balance)
            elif choice==2:
                amount=int(input("Enter the amount to be withdrawn: "))
                if amount<=balance:
                    balance-=amount
                else:
                    print("Insufficient Balance")
            elif choice==3:
                amount=int(input("Enter the amount to be deposited: "))
                balance+=amount
                print("Amount Deposited Successfully")
            elif choice==4:
                print("Thank You")
                break
            else:
                print("Invalid Choice")
        break
    else:
        attempts+=1
        print("Incorrect Pin")
else:
    print("Account Blocked")
'''

# SEAT AVAILABILITY SYSTEM
'''
seats=48
while seats>0:
    print("Available Seats: ",seats)
    booking_seat=int(input("Enter the number of seats needed: "))
    if booking_seat<=seats:
        seats-=booking_seat
        print("Seats Booked Successfully")
        remaining_seats=seats
        print("Remaining Seats: ",remaining_seats)
    else:
        print("Seats Not Available")
    choice=input("Do you want to continue (Yes/No): ").lower()
    if choice=="no":
        break
print("Booking Closed")
'''

# FIZZBUZZ PATTERN
'''
start_value=int(input("Enter start value: "))
end_value=int(input("Enter end value: "))
for i in range(start_value,end_value+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
'''

# FIND LARGEST AND SMALLEST ELEMENT IN A LIST
'''
numbers=[]
n=int(input("Enter the number of elements to be inserted: "))
for i in range(n):
    num=int(input(f"Enter the number {i+1}: "))
    numbers.append(num)
largest=numbers[0]
smallest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
print(f"Largest number in the list is {largest}")
print(f"Smallest number in the list is {smallest}")

# LOGIC 
10,15,21,3,8
largest = 10
smallest=10
num=10
num=15
10>15 False
10>15 True
largest=15
smallest=10
num=21
21>10
'''

# SEPERATE POSITIVE AND NEGATIVE NUMBER FROM THE LIST

# WORKING OF SPLIT()
''' 
"10 20 30 40 50"
USING SPLIT()--> "10" "20" "30" "40" "50" 
'''

# TUPLE
'''
numbers=tuple(map(int,input("Enter the numbers to be inserted: ").split()))
element=int(input("Enter the element to count: "))
count=0
for item in numbers:
    if item ==element:
        count+=1
print("Tuple Elements are ",numbers)
print(f"Occurence of {element} is: {count}")
'''

# SUM OF ELEMENT

'''
INPUT=1 2 3 4 5 6
TARGET=6
OUTPUT=[1,5][2,4][3,3]
'''

'''
numbers=tuple(map(int,input("Enter the numbers to be inserted: ").split()))
target=int(input("Enter the target sum: "))
for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        if numbers[i]+numbers[j]==target:
            print([numbers[i],numbers[j]])
'''

# REVERSE A DICTONARY

'''
INPUT data={"a":1,"b":2,"c":3}
OUTPUT data={"c":3,"b":2,"a":1}
'''

'''
data={"a":1,"b":2,"c":3}
reverse_data={}
keys=list(data.keys())
for key in keys[::-1]:
    reverse_data[key]=data[key]
#   reverse_data[data[key]]=key ---> another method
print("Reversed Data: ",reverse_data)
'''