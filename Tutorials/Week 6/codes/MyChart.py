option = int(input("Enter a number ?  "))
print(f"Multiplication chart for number {option}")

for multi in range(1, 13):
    new_value = multi * option
    print(f'''{option} x {multi} = {new_value}''')