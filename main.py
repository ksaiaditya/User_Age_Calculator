from datetime import datetime
dob = input("Enter your DOB as DD/MM/YYYY : ")
dob = datetime.strptime(dob, "%d/%m/%Y")
PD = datetime.now()
print("\nThe number of days the person is alive:", (PD - dob).days)