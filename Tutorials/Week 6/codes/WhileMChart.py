numba = int(input("Enter a number >> "))
print(f"Multiplication chart for number {numba}")

x = 0
while x < 12:
    x += 1
    multi = x * numba
    print(f"{x} x {numba} = {multi}")