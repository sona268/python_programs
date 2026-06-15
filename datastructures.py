'''username="Sona"
# 0  1  2  3
# S  o  n  a index always starts from zero (positive indexing)
#-4 -3 -2 -1
print("Username: ",username)
print(username[2])
print(username[-1])
print(username[3])


data="Python is a programming language"
print(data[1:8])
print(data[10:4:-2])
print(data[::-1])
print(data[6:])
print(data[:6])
print(data[::3])
print(data[::-2])


car="kia INNOVA"
print(car.upper())
print(car.lower())
print(car.capitalize())
print(car.title())

print(car.startswith("bac"))
print(car.endswith("VA"))
print(car.replace("kia","i10"))
car[2]="e"#string cannot be changed because it is immutable
print(car)
print(id(car))
uppercase=car.upper()
print(id(uppercase))


# LIST
user_data=['Sona','Kulathupuzha',22]
user_data.insert(2,"Oyoor")
user_data.append("friends")
user_data.extend("python")
user_data.append(["Malayalam","English","Hindi"])
user_data.extend(["SQL","Java","CS"])
user_data.remove("Sona")
#user_data.remove("fcfs")
user_data.pop(2)
user_data.reverse()
#user_data.sort()
print(user_data)
print(user_data[12])


# TUPLE
tuple1=(10,20,30,40)
print(tuple1)
nested_tuple=((4,5,6,7),21,"Sona","Goa")
print(nested_tuple)
# try out indexing and slicing 
# try out immutability


# TUPLE UNPACKING
person=("Sona",21,"Kulathupuzha")
name,age,place=person
print(name)
print(age)
print(place)


number=(10,20,30,40,50)
a,b,*c=number
print(a)
print(b)
print(*c)

d,*e,f=number 
print(d)
print(*e)
print(f)


value=(2,3,4,5,6,2,6,2,5,6,2,6)
print(len(value))# find the length
print(value.count(6))# find how many elements in the list
print(value.index(3))
print(value[3])


user_data=input("Enter a String: ")
count=0
for item in user_data:
    count+=1
print(count)


#PRINT FIRST NON REPEATING CHARACTER IN A STRING
user_input=input("Enter a String: ")
count=0
for item in user_input:
    if user_input.count(item)==1:
        print("First non repeating character is ",item)
        break
else:
    print("There is no non repeating character")


# SET
student1={"English","Hindi","Malayalam"}
student2={"English","Hindi","Python"}
student3={"Urdu","Python"}
student1.add("C") # ADD
#print(student1)
student1.update(["Jango","Css"]) # UPDATE
#print(student1)
#student1.add(["Java","Html","php"])
#print(student1)

student1.add("Malayalam") # DUPLICATE
print(student1)

student1.remove("Hindi") # REMOVE
print(student1)
#student1.remove("Javascript")
#print(student1)
student1.discard("Javascript") # DISCARD 
print(student1)


#UNION INTERSECTION DIFFERENCE 

student1={"English","Hindi","Malayalam"}
student2={"English","Hindi","Python"}
student3={"Urdu","Python"}
print(student1.union(student2))
print(student1.intersection(student2))
print(student1.difference(student2))


#USING SYMBOL

print(student1 | student2) # UNION
print(student1 & student2) # INTERSECTION
print(student1 - student2) #DIFFERENCE


# DISJOINT SET, SUPER SET, SUBSET

set1={1,2,3}
set2={7,8,9}
set3={4,5,6}
print(set1.isdisjoint(set2))
print(set2.isdisjoint(set1))


#FROZEN SET--> immutable, unordered and unique elements

fs1=frozenset("Sona")
fs2=frozenset([12,23,24])
fs3=frozenset((11,22,33))
print(fs1)
print(fs2)
print(fs3)


#DICTONARY

student={
    "name": "Sona",
    "age": 21,
    "place": "Kulathupuzha"
}
print(student)
print(student["name"])
print(student.get("marks"))
student["marks"]=55
print(student)
student.pop("age")
print(student)
del student["name"]
print(student)
student.update({"nationality":"Indian","state":"Kollam"})
print(student)

# try out update function for multiple insertion


# KEY VALUE PAIRS

info=dict(city="Kollam",location="Kerala")
print(info.keys())
print(info.values())
print(info)'''


# NESTED DICTONARY

employee={
    "emp1":{
        "name":"Sona",
        "age":21
    },
    "emp2":{
        "name":"Sumin",
        "age":24
    },
    "emp3":{
        "name":"Parvathy",
        "age":24
    },
    "emp4":{
        "name":"Zyan",
        "age":23
    }
}
print(employee["emp3"]["age"])