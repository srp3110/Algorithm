def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
value = int(input("Enter a non-negative interger >> "))
print("The fatorial of", value, "is", factorial(value))