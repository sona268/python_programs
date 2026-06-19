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

number=int(input("Enter the number: ")) 
corret_pin=1234
balance=50000
attempts=0
while attempts<=3:
    pin=int(input("Enter a pin: "))
    if pin==corret_pin:
        print("Login Successful")
        while True:
            print("")
            choice=int(input)
    else:
        print("Login Failed")