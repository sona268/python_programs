customer_name=input("Enter the customer name: ")
vehicle_number=input("Enter the vehicle number: ")
fuel_type=input("Fuel type is (Petrol/Diesel): ")
number_of_liters_filled=float(input("Enter the number of liters filled: "))
price_per_liter=float(input("Enter the price per liter: "))
premium_card=input("Has premium card or not (T/F): ")


total_fuel_amount=number_of_liters_filled*price_per_liter
gst=total_fuel_amount*0.05
final_bill_amount=total_fuel_amount+gst


final_bill_amount+=0
final_bill_amount-=0
final_bill_amount*=1


if premium_card and final_bill_amount>3000:
    final_bill_amount-=200
    print("200 IS DEDUCED")
else:
    print("NO DISCOUNT")


print("Datatype of customer name: ",type(customer_name))
print("Datatype of vehicle number: ",type(vehicle_number))
print("Datatype of fuel type: ",type(fuel_type))
print("Datatype of number of liters filled: ",type(number_of_liters_filled))
print("Datatype of price per liter: ",type(price_per_liter))
print("Datatype of premium card: ",type(premium_card))
print("Datatype of total fuel amount: ",type(total_fuel_amount))
print("Datatype of gst: ",type(gst))
print("Datatype of final bill amount: ",type(final_bill_amount))


print("Is liters float?",isinstance(number_of_liters_filled,float))
print("Is premium card boolean?",isinstance(premium_card,bool))


print("Id of total fuel amount: ",id(total_fuel_amount))
print("Id of total bill amount: ",id(final_bill_amount))


print("--------PETROL BILL--------")
print("Customer Name: ",customer_name)
print("Vehicle Number: ",vehicle_number)
print("Fuel Type: ",fuel_type)
print("Fuel Amount: ",total_fuel_amount)
print("GST Amount: ",gst)
print("Final Bill Amount: ",final_bill_amount)