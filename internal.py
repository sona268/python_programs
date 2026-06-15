#Online Shopping Management System

category={"Clothes","Electronics","Books","Accessories"}
item=input("Enter the item to be purchased: ")
product=int(input("Enter the number of product: "))
for item in range(product):
    name=input("Enter name: ")
    category=input("Enter category: ")
    price=input("Enter price: ")
total_bill=price*product
discount