"""Question 1"""

# age = int(input('Enter your age => '))

# if age >= 18:
#     print('You are eligible for voting')
# else:
#     print('You are not eligible for voting')

"""Question 2"""

# def calc():
#     units = float(input('Enter electric units => '))
#     if units <= 100:
#         print('No charge')
#     elif units > 100 and units <=200:
#         price = round((units - 100)*0.8, 2)
#     elif units > 200:
#         price = round((100*0.8) + ((units - 200)*1.5), 2)
#     return price

# print(f'Your total bill amount is RM{calc()}')

"""Question 3"""

# num = 0
# while num < 11:
#     num = int(input("Enter a number => "))

"""Question 4"""

# student_list = [{"std_id":"035721","cgpa":"3.4"},
# {"std_id":"036013","cgpa":"2.8"},
# {"std_id":"039026","cgpa":"2.2"},
# {"std_id":"037843","cgpa":"4.0"},
# {"std_id":"031284","cgpa":"3.7"},
# {"std_id":"038032","cgpa":"1.8"}
# ]
# count = 1

# print('The list of students with CGPA more than 3.0 >>')

# for element in student_list:
#     if float(element["cgpa"]) > 3.0:
#         print(f'{count}. {str(element["std_id"])}')
#         count += 1

"""Question 5"""

# data = [-2, 1, 1, 3, 3, 3, 4, 5, 6, 78, 78, 79] 
# new_data =[]

# def remove_duplicates(data):
#     for num in data:
#         if num not in new_data:
#             new_data.append(num)
#     return new_data

# print(f'data = {remove_duplicates(data)}')

"""Question 6"""

# def power(a,b):
#     if a == 0:
#         return 0
#     elif b == 1:
#         return a
#     elif b == 0:
#         return 1
#     else:
#         return a*power(a,b-1)

# a = int(input("Enter base number => "))
# b = int(input("Enter power number => "))
# print(f'{a} to the power of {b} is {power(a,b)}')