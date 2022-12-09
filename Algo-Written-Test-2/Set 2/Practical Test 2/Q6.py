def power(a,b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)


# a = 4
# b = 5
# print(power(a,b))

base = int(input("Enter the base number"))
expo = int(input("Enter the power number"))
print(power(base, power))

