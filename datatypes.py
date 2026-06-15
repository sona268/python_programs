'''student_name=input("Enter the student name: ")
student_id=int(input("Enter the student id: "))
student_mark=float(input("Enter the student mark: "))
is_present=bool(input("Is present or not(T/F): "))
languages_known=input("Enter the languages known: ").split(",")

print("The student name is ",student_name)
print("The student id is ",student_id)
print("The student mark is ",student_mark)
print("present or not ",is_present)
print("Languages known are ",languages_known)

print(type(student_name))
print(type(student_id))
print(type(student_mark))
print(type(is_present))
print(type(languages_known))'''

num1=10
num2=10
print(id(num1))
print(id(num2))

list1=[10,20]
list2=[10,20]
print(id(list1))
print(id(list2))

print(isinstance(num1,int))
print(isinstance(list1,list))
print(isinstance([100,200],list))
print(isinstance(list1[0],int))