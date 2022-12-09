def maxNumber(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    elif a == b and a > c:
        return a
    elif a == c and a > b:
        return a
    elif b == c and b > a:
        return b
a = int(input("Enter first number >> "))
b = int(input("Enter second number >> "))
c = int(input("Enter third number >> "))
print("The maximum number is", maxNumber(a,b,c))