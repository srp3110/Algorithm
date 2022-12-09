"""Question 1"""

# mark = int(input('Enter your mark => '))

# if mark >= 80 and mark <= 100:
#     print('Your grade is an A')
# elif mark >=60 and mark <= 79:
#     print('Your grade is an B')
# elif mark >=40 and mark <= 59:
#     print('Your grade is an C')
# elif mark >=0 and mark <= 39:
#     print('Your grade is an F')
# else:
#     print('Enter a valid mark')

"""Question 2"""

# a = int(input('Enter the first side length of the triangle => '))
# b = int(input('Enter the second side length of the triangle => '))
# c = int(input('Enter the third side length of the triangle => '))

# if a == b and b == c and a == c:
#     print('This is an equilateral triangle')
# elif a != b and b != c and a != c:
#     print('This is a scalene triangle')
# else:
#     print('This is an isosceles triangle')

"""Question 3"""

# num = 0

# while num < 51:
#     num = int(input('Enter a number => '))

"""Question 4"""

# Student =[{"course":"Malay","mark":"75.6"},
# {"course":"English","mark":"56.4"},
# {"course":"Mathematics","mark":"81.2"},
# {"course":"Science","mark":"68.8"},
# {"course":"History","mark":"99.4"},
# {"course":"Arts","mark":"24.0"}
# ]
# count = 1

# print('The courses that the student scores more than 70 >>')
# for elements in Student:
#     if float(elements["mark"]) > 70:
#         print(f'{count}. {str(elements["course"])}')
#         count += 1

"""Question 5"""

# day = 1
# count = 0
# listTemp = []
# totalTemp = 0
# aboveAvg = 0

# while True:
#     temp = input(f"Day {day}'s high temp: ")
#     day += 1
#     if temp == "done":
#         break
#     listTemp.append(float(temp))

# for values in listTemp:
#     totalTemp += values
#     count += 1

# avgtemp = round(totalTemp/count, 1)
# for values in listTemp:
#     if values > avgtemp:
#         aboveAvg += 1

# print(f'Average temp = {avgtemp}')
# print(f'{aboveAvg} days were above average')

"""Question 6"""
