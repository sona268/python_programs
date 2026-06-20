import json
import pickle
import os
student=[]
while True:
    print("\n------ STUDENT RECORD MANAGEMENT SYSTEM ------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Save as JSON")
    print("4. Save as Pickle")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter Student Name: ")
        rollno=input("Enter Roll Number: ")
        record={
            "Name": name,
            "RollNo": rollno
        }
        student.append(record)
        student_record=open("student.txt", "a")
        student_record.write(f"{name} {rollno} ")
        print("Student Added Successfully")
        print("File Name: ",student_record.name)
        print("File Mode: ",student_record.mode)
        print("File Closed Status: ",student_record.closed)
        print("Current File Pointer Position: ",student_record.tell())
        student_record.close()
    elif choice==2:
        try:
            student_record=open("student.txt","r")
            print("Student Records")
            data=student_record.read()
            print(data)
            student_record.close()
        except FileNotFoundError:
            print("No Records Found")
    elif choice==3:
        student_record=open("student.json","w")
        json.dump(student,student_record,indent=4)
        student_record.close()
        print("JSON File Created Successfully")
    elif choice==4:
        student_record=open("student.pkl","wb")
        pickle.dump(student,student_record)
        student_record.close()
        print("Pickle File Created Successfully")
    elif choice==5:
        print("Directory Contents:")
        print(os.listdir())
        try:
            student_record= open("student.json","r")
            data=json.load(student_record)
            print("Student Records Loaded Successfully")
            print(data)
            student_record.close()
        except:
            pass
        print("Operation completed")
        break
    else:
        print("Invalid Choice")