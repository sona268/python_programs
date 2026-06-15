#Employee Salary Report Generator

total_salary=0
for i in range(1,6):
    salary=float(input(f"Enter Salary of Employee {i}: "))
    total_salary+=salary
print("Total Salary Expenditure: ₹",total_salary)


#Student Attendance Counter

present=0
absent=0
for student in range(1,11):
    attendance_status=input(f"Student {student} Attendence: ")
    if attendance_status=="P":
        present+=1
    else:
        absent+=1
print("Total Present Students: ",present)
print("Total Absent Students: ",absent)


#Supermarket Billing System

total_bill_amount=0
for item in range(1,6):
    price=float(input(f"Item {item} Price: "))
    total_bill_amount+=price
print("Total Bill Amount: ₹",total_bill_amount)


#Cricket Score Analyzer

run_scored=0
for ball in range(1,7):
    run=int(input(f"Ball {ball} Runs: "))
    run_scored+=run
print("Total Runs Scored: ",run_scored)


#Library Book Collection Counter

total_books=0
for section in range(1,8):
    book=int(input(f"Section {section} Books: "))
    total_books+=book
print("Total Books in Library: ",total_books)


#Online Exam Marks Calculator

total_marks=0
average_marks=0
for subject in range(1,6):
    marks=float(input(f"Subject {subject} Marks: "))
    total_marks+=marks
    average_marks=total_marks/5
print("Total Marks: ",total_marks)
print("Average Marks: ",average_marks)


#Daily Temperature Monitor

highest_temperature=0
for day in range(1,8):
    temperature=float(input(f"Day {day} Temperature: "))
    if temperature>highest_temperature:
        highest_temperature=temperature
print("Highest Temperature: ",highest_temperature,"°C")


#Mobile Recharge Collection System

total_collection=0
for customer in range(1,11):
    recharge=int(input(f"Customer {customer} Recharge: "))
    total_collection+=recharge
print("Total Collection: ₹",total_collection)


#Water Consumption Tracker

water_consumed=0
for day in range(1,8):
    consumption=float(input(f"Day {day} Consumption: "))
    water_consumed+=consumption
print("Total Water Consumption: ",water_consumed, "Litres")


#Factory Production Report'''

total_annual_production=0
for month in range(1,13):
    production=int(input(f"Month {month} Production: "))
    total_annual_production+=production
print("Total Annual Production: ",total_annual_production, "Units")