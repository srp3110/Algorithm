def genderDay():
    print("Enter your gender: M for Male and F for Female")
    gender = (input("Enter gender >> ")).lower()
    print("Enter the number of days worked")
    days = int(input("Enter days >> "))
    return gender, days
print("Enter an age from 18 to 40")
age = int(input("Enter age >> "))
if age >=18 and age <= 29:
    gender, days = genderDay()
    if gender == "m":
        totalWage = 700 * days
        print("Total wage is", totalWage)
    elif gender == "f":
        totalWage = 750 * days
        print("Total wage is", totalWage)
elif age >= 20 and age <= 40:
    gender, days = genderDay()
    if gender == "m":
        totalWage = 800 * days
        print("Total wage is", totalWage)
    elif gender == "f":
        totalWage = 850 * days
        print("Total wage is", totalWage)
    else: 
        print("Invalid gender entered")
else:
    print("Enter appropriate age")