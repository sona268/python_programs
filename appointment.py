from datetime import date
import random
def appointment_details():
    print("Appointment Date: ",date.today())
    token=random.randint(1000,9999)
    print("Generated Token Number: ",token)