"""Question 1"""

# a = input("Enter a number => ")
# b = input("Enter a number => ")
# c = input("Enter a number => ")

# def max(a,b,c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b>= c:
#         return b
#     else:
#         return c

# print(f'The maximum number is {max(a,b,c)}')

"""Question 2"""

# def calc():
#     tax = salary*0.05
#     return tax

# while True:
#     salary = int(input("Enter your salary => "))
#     if salary == -1:
#         print('Ending Program')
#         break
#     elif salary > 0:
#         calc()
#         print(f'Your income tax is {calc()}')
#     else:
#         print('Enter a valid value!!!')

"""Question 3"""

# age = int(input('Enter your age => '))
# gender = str.upper(input('Enter your gender M for Male and F for Female => '))
# days = int(input('Enter number of days worked => '))

# if age >= 18 and age <= 29 and gender == "M":
#     wage = 700*days
#     print(f'Your wage is {wage}')
# elif age >= 18 and age <= 29 and gender == "F":
#     wage = 750*days
#     print(f'Your wage is {wage}')
# elif age >= 30 and age <= 40 and gender == "M":
#     wage = 800*days
#     print(f'Your wage is {wage}')
# elif age >= 30 and age <= 40 and gender == "F":
#     wage = 850*days
#     print(f'Your wage is {wage}')
# else:
#     print('Enter appropriate age')

"""Question 4"""

# employee_list = [{"employee_name":"Sarah","salary":"28000"},
# {"employee_name":"Jonathan","salary":"80000"},
# {"employee_name":"Dylan","salary":"57000"},
# {"employee_name":"Benjamin","salary":"32000"},
# {"employee_name":"Alice","salary":"20000"},
# {"employee_name":"Rosa","salary":"89000"}
# ]
# count = 1

# print('The list of employees with salary more than 50,000 >>')

# for elements in employee_list:
#     if int(elements["salary"]) > 50000:
#         print(f'{count}. {str(elements["employee_name"])}')
#         count+=1

"""Question 5"""

# print('Type in the GPA for each semester or "done" to finish')
# count = 0
# sem = 1
# list_gpa = []
# totalGPA = 0
# aboveAverage = 0

# while True:
#     option = input(f'Semester {sem} GPA: ')
#     sem+=1
#     if option == "done":
#         break
#     list_gpa.append(float(option))

# for values in list_gpa:
#     totalGPA += values
#     count += 1

# averageGPA = round(totalGPA/count, 2)
# for values in list_gpa:
#     if values > averageGPA:
#         aboveAverage += 1
# print ("")
# print(f'Average GPA = {averageGPA}')
# print(f'{aboveAverage} semester were above average.')

"""Question 6"""

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial(n-1)

# num = int(input('Enter a non-negative number => '))
# print(f"The factorial of {num} is {factorial(num)}")