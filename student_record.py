import pickle
import json
student=["Ammu","Chikku","Pooja"]
student_record=open("student.txt","r")
print(student_record.)
student_record.close()




# Student Details
name = input("Enter Student Name: ")


# Write to Text File
file = open("student.txt", "w")
file.write("Name: " + name + "\n")
file.write("Roll No: " + rollno)
file.close()

print("Data Written Successfully")

# Read from Text File
file = open("student.txt", "r")
print("\nStudent Details")
print(file.read())
file.close()

# JSON Serialization
student = {
    "Name": name,
    "RollNo": rollno
}

file = open("student.json", "w")
json.dump(student, file)
file.close()

print("\nJSON File Created")

# Pickle Serialization
file = open("student.pkl", "wb")
pickle.dump(student, file)
file.close()

print("Pickle File Created")


------ STUDENT RECORD MANAGEMENT SYSTEM ------
1. Add Student
2. View Students
3. Save as JSON
4. Save as Pickle
5. Exit
Student Added Successfully
File Name:
students.txt
File Mode:
r+
File Closed Status:
False
Current File Pointer Position:
25
Directory Contents:
['students.txt', 'attendance.txt']
JSON File Created Successfully
Pickle File Created Successfully
Student Records Loaded Successfully
Operation completed