'''store_data=open("newfile.txt","w")
store_data.write("Welcome to python programming")
print(store_data)
store_data.close()'''

'''read_data=open("newfile.txt","r")
print(read_data.read())
read_data.close()'''

'''append_data=open("newfile.txt","a")
append_data.write("\nPython is an iterpreted language")
print(append_data)
append_data.close()

read_data=open("newfile.txt","r")
print(read_data.read())
read_data.close()'''


# USING CONTEXT MANAGER
'''
with open("newfile.txt","r") as f:
    print("Current Position: ",f.tell())
    f.read(6)
    print("After Read Position: ",f.tell())
    f.seek(4)
    print("After Seek: ",f.tell())
    print(f.read())

with open("cherryblossom.jpg","rb") as read_data:
    image_read=data.read()
    print(image_read)


# TRY OUT PIP INSTALL PILLOW AND USE ITS FUNCTIONS, USE PILLOW TO IMPORT IMAGE

tech=open("delete_file.txt","x")
print(tech)
tech.close()

file_path="delete_file.txt"
import os
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted successfully")
else:
    print("File does not exist")


# SERIALIZATION AND DESERIALIZATION

import pickle
data={
    "students":["Raju","Chinnu","Ammu"],
    "marks":(79,85,93),
    "subjects":{"Maths","Hindi","English"}
    }

# SERIALIZATION- SAVING DATA TO FILE

with open("user_details.pkl","wb") as f:
    pickle.dump(data,f)
print("Data is serialized into user details",data)

with open("user_details.pkl","rb") as file:
    loaded_data=pickle.load(file)
    print("Data read from the pickle: ",loaded_data)


# SERIALIZATION- SAVING DATA TO MEMORY

dump_data=pickle.dumps(data)
print("Data is serialized to bytes: ",dump_data)

load_data=pickle.loads(dump_data)
print("Data is deserialized to objects:",load_data)

# TRY OUT JSON MODULE'''