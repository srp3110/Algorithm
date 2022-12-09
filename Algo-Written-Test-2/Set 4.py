"""Question 1"""

# num = int(input('Enter a non-negative number => '))

# if num >= 0:
#     if num % 4 == 0 and num % 9 == 0:
#         print(f'{num} is divisible by both 4 and 9')
#     else:
#         print(f'{num} is not divisible by both 4 and 9')
# else:
#     print('Enter a non-negative number')

"""Question 2"""

# print('''Type in a your GPA for each semester or "done" to calculate your final 
# CGPA''')
# count = 1
# listGPA = []
# totalGPA = 0
# gpaCount = 0
# cgpa = 0
# while True:
#     sem = input(f'Semester {count} GPA: ')
#     count += 1
#     if sem == "done":
#         break
#     listGPA.append(float(sem))
# for values in listGPA:
#     totalGPA += values
#     gpaCount += 1
# cgpa = round(totalGPA/gpaCount, 2)
# print('')
# print(f'Your CGPA is {cgpa}')

"""Question 3"""

# name = str(input('Employee Name >> '))
# days = int(input(f'Number of days {name} worked >> '))
# ttl_days = int(input(f'Number of days {name} should be working >> '))

# attendance = round(float(days/ttl_days)*100, 2)

# print('')
# if attendance > 80:
#     print(f'{name} can receive a raised (Attendance: {attendance}%)')
# else:
#     print(f'{name} cannot receive a raised (Attendance: {attendance}%)')

"""Question 4"""

# employee_list = [{"employee_name":"Sarah","preferred_work":"online"},
# {"employee_name":"Jonathan","preferred_work":"onsite"},
# {"employee_name":"Dylan","preferred_work":"onsite"},
# {"employee_name":"Benjamin","preferred_work":"online"},
# {"employee_name":"Alice","preferred_work":"onsite"},
# {"employee_name":"Rosa","preferred_work":"online"}
# ]
# count = 1

# print('The list of employees that preferred to work onsite >>')
# for elements in employee_list:
#     if str(elements["preferred_work"]) == "onsite":
#         print(f'{count}. {str(elements["employee_name"])}')
#         count += 1

"""Question 5"""

# def remove_duplicated():

# data = [-2, 1, 1, 3, 3, 3, 4, 5, 6, 78, 78, 79] 
# newData = []
# for i in data:
#     if i not in newData:
#         newData.append(i)

# print(f'Data = {newData}')

"""Question 6"""

# list_num = [90, 34, 67, 12, 59]

# def sumList(n):
#     if len(n) == 1:
#         return n[0]
#     else:
#         return n[0] + sumList(n[1:])

# print(sumList(list_num))