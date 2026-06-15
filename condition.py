#Smart ATM Authentication System

pin=int(input("Enter the pin: "))
balance=float(input("Enter the amount: "))
withdrawal_amount=float(input("Enter the withdrawal amount: "))
stored_pin=1234
if pin==stored_pin:
    if balance>withdrawal_amount:
        balance-=withdrawal_amount
        print("Withdrawal Successful")
        print("Remaining balance: ",balance)
    else:
        print("Insufficient Balance")
else:
    print("Incorrect Pin")


#Online Shopping Discount Calculator

purchase_amount=float(input("Enter Purchase Amount: "))
premium_member=input("Premium Member (yes/no): ")
if premium_member=="yes":
    if purchase_amount>10000:
        discount=25
    elif purchase_amount>=5000:
        discount=15
    else:
        discount=5
else:
    discount=0
discount_amount=(purchase_amount*discount)/100
final_bill_amount=purchase_amount-discount_amount
print("Discount Applied: ",discount,"%")
print("Final Bill Amount: ",final_bill_amount)


#University Admission Eligibility Checker

higher_secondory=float(input("Enter higher secondary percentage: "))
mathematics=float(input("Enter mathematics percentage: "))
entrance_score=float(input("Enter entrance exam score: "))
if higher_secondory>75 and mathematics>70 and entrance_score>80:
    print("Admission Status: Eligible")
    print("Suggested Course: Computer Science")
else:
    print("Admission Status: Not Eligible")


#Loan Approval System

age=int(input("Enter Age: "))
salary=int(input("Enter Salary: "))
credit_score=int(input("Enter Credit Score: "))
existing_loan=input("Existing Loan (yes/no): ")
if age>=18 and salary>=25000 and credit_score>700 and existing_loan=="no":
    print("Loan Status: Approved")
else:
    print("Loan Status: Rejected")


#Hospital Patient Priority System

age=int(input("Enter Age: "))
condition=input("Enter Condition (critical/severe/mild): ")
if condition=="critical":
    print("Emergency")
elif condition=="severe":
    print("High Priority")
else:
    print("Normal Priority")


#Employee Bonus Management System

years_of_service=int(input("Enter Years of Service: "))
performance=input("Enter Performance Rating (Excellent/Good/Average): ")
attendance=float(input("Enter Attendance Percentage: "))
salary=float(input("Enter Salary: "))
if years_of_service>=5 and performance=="Excellent" and attendance>=90:
    bonus_percentage=20
elif years_of_service>=3 and performance=="Good":
    bonus_percentage=10
else:
    bonus_percentage=5
bonus_amount = salary * bonus_percentage / 100
print("Bonus Percentagr: ",bonus_percentage,"%")
print("Bonus Amount: ₹",bonus_amount)


#Smart Traffic Fine System

helmet=input("Helmet Worn (yes/no): ")
seatbelt=input("Seatbelt Used (yes/no): ")
speed_limit=input("Speed Limit Violated (yes/no): ")
valid_license=input("Valid License (yes/no): ")
fine=0
if helmet=="no":
    fine+=500
if seatbelt=="no":
    fine+=500
if speed_limit=="yes":
    fine+=1000
if valid_license=="no":
    fine+=2000
print("Total Fine: ₹",fine)


#Cinema Ticket Booking System

age=int(input("Enter Age: "))
seat=input("Seat Type (Normal/Premium): ")
day=input("Day Type (Weekday/Weekend): ")
student=input("Student (yes/no): ")
price=0
if seat=="Premium":
    price=300
else:
    price=200
if day=="Weekend":
    price+=50
else:
    price=200
if student=="yes":
    price-=20
else:
    price=200
print("Final Ticket Cost: ₹",price)


#Scholarship Eligibility System

income=int(input("Enter Family Income: "))
academic=float(input("Enter Academic Percentage: "))
attendance=float(input("Enter Attendance Percentage: "))
if income<=200000 and academic>=90 and attendance>=80:
    print("Scholarship Status: Full Scholarship")
elif income<=250000 and academic>=85:
    print("Scholarship Status: Partial Scholarship")
else:
    print("Scholarship Status: No Scholarship")


#Student Performance Analytics System

mark1=float(input("Enter Mark 1: "))
mark2=float(input("Enter Mark 2: "))
mark3=float(input("Enter Mark 3: "))
mark4=float(input("Enter Mark 4: "))
mark5=float(input("Enter Mark 5: "))
total_mark=mark1+mark2+mark3+mark4+mark5
percentage=total_mark/5
if percentage>=90:
    grade="A+"
elif percentage>=80:
    grade="A"
elif percentage>=70:
    grade="B+"
elif percentage>=60:
    grade="B"
elif percentage>=50:
    grade="C+"
elif percentage>=40:
    grade="C"
else:
    grade="Fail"
if percentage>=40:
    result= "Pass"
    promotion_status= "Eligible"
else:
    result= "Fail"
    promotion_status= "Not Eligible"
print("Total Marks: ",total_mark)
print("Percentage: ",percentage)
print("Grade: ",grade)
print("Result: ",result)
print("Promotion Status: ",promotion_status)