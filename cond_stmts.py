'''#Syntax of if else

if condition:
    code to be executed
else:
    code to be executed


#Syntax of if elif else

if condition:
    code to be executed
elif condition:
    code to be executed
else:
    code to be executed


#Positive or negative

num=int(input("Enter the number: "))
if num>0:
    print("Positive Number")
else:
    print("Negative Number")


#Vowels or consonants

vowel_check=input("Enter a character: ")
if vowel_check in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")


#odd or even

odd_even=int(input("Enter the number: "))
if odd_even%2==0:
    print("Even number")
else:
    print("Odd number")


#Child Teenager Senior

age=int(input("Enter the age:"))
if age<13:
    print("Child")
elif age<18:
    print("Teenager")
elif age<60:
    print("Adult")
else :
    print("Senior citizen")


#To check whether the given number id positive and even or positive and odd otherwise negative

num=int(input("Enter the number: "))
if num>0:
    if num%2==0:
        print("Number is positive and even")
    else:
        print("Nunber is positive and odd")
else:
    print("Number is negative")


#Three digit number

a=int(input("Enter a number: "))
if a>99 and a<1000:
    print("The number is a three digit number")
else:
    print("The number is not a three digit number")

#Three digit number another method

threedigit=int(input("Enter a number: "))
if 99<threedigit<1000:
    print("The number is three digit")
else:
    print("The number is not three digit")'''


#Simple ATM program

balance_amount=50000
withdrawal_amount=int(input("Enter the withdrawal amount: "))
if withdrawal_amount<balance_amount:
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")