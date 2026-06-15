customer_name=input("Enter Customer Name: ")
mobile_number=int(input("Enter Mobile Number: "))
food_item=input("Enter Food Item: ")
quantity=input("Enter Quantity: ")
price_per_item=float(input("Enter Price Per Item: "))
delivery_distance=float(input("Enter Delivery Distance: "))
premium_member=bool(input("Premium Member (True/False): "))

def calculate_food_amount(quantity,price):
    total_amount=quantity*price
    return total_amount
print("Total Amount= ₹",total_amount)
calculate_food_amount(quantity,price)

def calculate_delivery_charge(distance):
    if distance<5:
        return 40
    else:
        return 80
total_amount+=delivery_charge
print("Delivery Charge: ₹",total_amount)
calculate_delivery_charge(distance)

def calculate_discount(bill_amount, premium_member):
    if customer==premium_member and bill_amount>1000:
        return 150
    else:
        return 0
discount-=total_amount
print("Discount Amount: ₹",discount)
calculate_discount(bill_amount,premium_member)

def generate_bill(**customer_details):
    print("Customer Details: ")





Sample Output
Enter Customer Name: Rahul
Enter Mobile Number: 9876543210
Enter Food Item: Pizza
Enter Quantity: 3
Enter Price Per Item: 250
Enter Delivery Distance: 6
Premium Member (True/False): True
----------- FOOD ORDER BILL -----------
Customer Name: Rahul
Mobile Number: 9876543210
Food Item: Pizza
Food Amount: ₹750
Delivery Charge: ₹80
Discount: ₹0
Final Bill Amount: ₹830
Datatype of Quantity: <class 'int'>
Datatype of Price: <class 'float'>
Datatype of Premium Member: <class 'bool'>
Is Quantity Integer? True
Is Price Float? True
Is Premium Member Boolean? True
ID of Food Amount: 12345678
ID of Final Bill Amount: 87654321
Offer: Free Soft Drink on Orders Above ₹1500
Food Search Result: Pizza