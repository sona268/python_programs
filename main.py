import patient
import doctor
import billing
import appointment as ap
import sys
import importlib
print("------ HOSPITAL MANAGEMENT SYSTEM ------")
patient.patient_details()
doctor.doctor_details()
ap.appointment_details()
billing.billing_details()
print("Current Module Name: ")
print(__name__)
print("Imported Modules:")
print(patient.__name__)
print(doctor.__name__)
print(billing.__name__)
print("Python Search Paths: ")
print(sys.path)
importlib.reload(patient)
print("Module Reloaded Successfully")
print("Thank You for Using Hospital Management System")