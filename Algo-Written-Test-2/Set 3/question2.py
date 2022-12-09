option = 0
print("Enter -1 to end the program")
while option != -1:
    option = float(input("Enter your salary income >> "))
    incomeTax = round(option*0.05,2)
    print("Your income tax is", incomeTax)
print("Ending program...")