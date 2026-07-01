'''class Student:
    def display(self): # self represents the current object or instance of a class
        print("I am a student")
student=Student() # object creation
student.display()

class Employee:
    def __init__(self): # init is a constructor. Constructors are used for initializing objects and it is called when the object is created
        print("Default constructor is called")
emp=Employee()

class Car:
    colour="Black" #class variable
    def __init__(self,brand,model):
        self.brand=brand # instance variable
        self.model=model 
car=Car("Porsche",911)
print(car.brand,car.model,car.colour)

car1=Car("BMW","M5")
print(car1.brand,car1.model)

# self
# Each object maintains its own data
# Method can access object properties
# Without self cannot acces object variables
# Cannot store data seperately for each object
# Method cannot know which object called them

class Library:
    def __init__(self,name,location="Trivandrum",total_books=0):
        self.name=name
        self.location=location
        self.total_books=total_books
library=Library("Anna")
print(library.name,library.location,library.total_books)

library1=Library("Chinnu","Kollam")
print(library1.name,library1.location,library1.total_books)

library2=Library("Dona","Kochi",5)
print(library2.name,library2.location,library2.total_books)
'''

# SINGLE INHERITANCE
'''
class User: # Parent class/Super class/Base class
    def login(self):
        print("User logged in")

class Influencer(User): # Child class/Sub class/Derived class
    def post_reels(self):
        print("Influencer posted a new reel")

influencer=Influencer()
influencer.login()
influencer.post_reels()
'''

# MULTILEVEL INHERITANCE --> Middle class acts as child and parent
'''
class Vehicle:
    def category(self,mode):
        print("Mode of transport: ",mode)

class Car(Vehicle):
    def vehicle_category(self,category,color):
        print("Type of car: ",category)
        print("Color of car: ",color)

class ElectricCar(Car):
    def car_type(self,brand,category,varient,price):
        print(" Car brand: ",brand)
        print("Car category: ",category)
        print("Car varient: ",varient)
        print("Price of car: ",price)

electriccar=ElectricCar()
electriccar.category("Road")
electriccar.vehicle_category("Car","Black")
electriccar.car_type("Tesla","Electric vehicle","Latest model","500000")
'''

# MULTIPLE INHERITANCE
'''
class ImageUpload:
    def upload(self,user_name,picture_name):
        print(f"The picture {picture_name} from {user_name} uploaded successfully")

class ReelUpload:
    def upload(self,user_name,reel_name):
        print(f"{user_name} uploaded {reel_name}")

class Instagram(ImageUpload,ReelUpload):
    def user_analytics(self,user_name,owner,reaction):
        print(f"{user_name} is having a {owner} account with {reaction} reactions on post uploaded today")

instagram=Instagram()
instagram.upload("THV","image.img")
instagram.upload("THV","Promotion reel")
instagram.user_analytics("THV","META",10000)
'''

# HYBRID INHERITANCE
'''
class Person:
    def person_details(self,name,age):
        print("Name of person: ",name)
        print("Age of person: ",age)

class Doctor(Person):
    def doctor_details(self):
        print("Doctor: Dr. Arun")

class Patient(Person):
    def patient_details(self):
        print("Patient ID: P101")

class MedicalRecord(Doctor, Patient):
    def record_details(self):
        print("Diagnosis: Fever")

medicalrecord=MedicalRecord()

obj.person_details()
obj.doctor_details()
obj.patient_details()
obj.record_details()
'''

# HIERARCHICAL INHERITANCE
'''
class Person:
    def person_details(self):
        print("Name: Ammu")
        print("Age: 20")

class Student(Person):
    def student_details(self):
        print("Course: BCA")

class Teacher(Person):
    def teacher_details(self):
        print("Subject: Python")

class Principal(Person):
    def principal_details(self):
        print("Designation: Principal")

student=Student()
teacher=Teacher()
principal=Principal()

print("Student Details")
student.person_details()
student.student_details()

print("\nTeacher Details")
teacher.person_details()
teacher.teacher_details()

print("\nPrincipal Details")
principal.person_details()
principal.principal_details()
'''

# POLYMORPHISM--> 2 types method overloading and overriding

# METHOD OVERLOADING
'''
print(len("Christeena"))
print(len([20,10,40,5]))
'''

# CALCULATOR
'''
class Calculator:
    def add(self,num1=0,num2=0,num3=0):
        return num1+num2+num3

calculator=Calculator()
print(calculator.add())
print(calculator.add(10))
print(calculator.add(10,20))
print(calculator.add(10,20,30))
'''

# FACEBOOK LOGIN
'''
class Facebook:
    def login(self,email=None,password=None,phone_number=None):
        if email and password:
            print(f"Login through email id: {email}")
        elif phone_number and password:
            print(f"Login through phone number: {phone_number}")
        else:
            print("Invalid Login")
facebook=Facebook()
facebook.login(email="ganga@yahoo.com",password="ganga0543")
facebook.login(phone_number=8546720295,password="ganga0543")
'''

# PAYMENT
'''
class Payment:
    def pay(self,amount,method="cash"):
        if method=="cash":
            print(f"{amount} is collected via {method} method")
        elif method=="upi":
            print(f"{amount} is collected via {method} method")
        elif method=="card":
            print(f"{amount} is collected via {method} method")
payment=Payment()
payment.pay(540)
payment.pay(450,method="upi")
payment.pay(350,method="card")
'''

# METHOD OVERRIDING
'''
class Employee:
    def work(self):
        print("Working as Employee")

    def skill(self):
        print("Python Full Stack Intern")

class Manager(Employee):
    def work(self):
        super().work()
        print("Managing team")

manager=Manager()
manager.work()
manager.skill()
'''

# ONLINE PAYMENT
'''
class Order:
    def order_details(self,product_name,quantity):
        print(f"Order placed for {quantity} {product_name}")

class OnlineOrder(Order):
    def order_details(self,product_name,quantity,address):
        super().order_details(product_name,quantity)
        print(f"Order delivered to {address}")

onlineorder=OnlineOrder()
onlineorder.order_details("Toblerone",2,"College Junction")
'''

# ABSTRACTION

from abc import ABC,abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    def headlights_on(self):
        print("Headlights are set to low")

class Car(Vehicle):
    def start_engine(self):
        print("Car started using key")
    def stop_engine(self):
        print("Engine stopped using key")

vehicle=Vehicle()
vehicle.start_engine()
vehicle.stop_engine()
vehicle.headlights_on()
'''
car=Car()
car.start_engine()
car.stop_engine()
car.headlights_on()'''