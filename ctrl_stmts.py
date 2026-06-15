'''#SYNTAX OF FOR LOOP
for variable in sequence:
    code to be executed


word=input("Enter a word: ")
for letter in word:
    print(letter,end="")


for element in [1,2,3,4]:
    print(element)


#USING RANGE FUNCTION

for variable in range(start,stop,skip):
    code to be executed


for element in range(11):
    print(element)


for element in range(5,16):
    print(element)


for element in range(10,26,5):
    print(element)


for element in range(1,10,-1):
    print(element) #It will not work


for element in range(10,0,-1):
    print(element)


for element in range(17,3,-3):
    print(element)


#MULTIPLICATION TABLE

num=int(input("Enter a number: "))
for i in range(1,11):
    print(i,"*",num,"=",i*num)
    
#printing using formatting string 
    print(f"{i} * {num} = {num*i}")


#WHILE LOOP
initialization
while condition:
    code to be executed
    updation


value=1
while value<=10:
    print(value)
    value+=1


value=1
sum=0
iteration=int(input("Enter the number of iteration: "))
while value<=iteration:
    sum+=value
    value+=1
print(sum)


#REVERSE A STRING

STEP 1: GETTING THE LAST DIGIT 
165 % 10 = 5
STEP 2: REMOVE THE LAST DIGIT
165 / 10 = 16
STEP 3:BUILT REVERSED NUMBER 
REVERSE = 0
REVERSE = REVERSE * 10 + DIGIT


number=int(input("Enter the number to be reversed: "))
reverse=0
while number>0:
    remainder=number%10
    reverse=reverse*10+remainder
    number//=10
print(reverse)


NUMBER=165
165 > 0 IS TRUE
REMINDER 165 % 10 IS 5
REVERSE= 0 * 10 + 5 = 5
NUMBER = 165 // 10 = 16
STILL NUMBER 16 IS GREATER THAN 0

NUMBER=16
16 > 0 IS TRUE
REMINDER 16 % 10 IS 6
REVERSE= 5 * 10 + 6 = 56
NUMBER = 16 // 10 = 1
STILL NUMBER 1 IS GREATER THAN 0

NUMBER=1
1 > 0 IS TRUE
REMINDER 1 % 10 IS 1
REVERSE= 56 * 10 + 1 = 561
NUMBER = 1 // 10 = 0
EXIT WHILE'''


#TO FIND THE NUMBER OF 9'S FROM 1 TO 100 

count=0
for number in range(1,101):
    temp=number
    while temp>0:
        digit=temp%10
        if digit==9:
            count+=1
        temp//=10
print("Total Number of 9: ",count)