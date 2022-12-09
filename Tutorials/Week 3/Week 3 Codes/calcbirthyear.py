def birthyear_please(y):
    Age = 2022 - int(y)
    return Age

y = input("Your birth year please >>")
Age = birthyear_please(y)

print("Your age is", Age)