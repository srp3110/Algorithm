""" Question 1
////////// """

# games = [{"Title": "Pokemon Sword", "Genre": "fantasy", "Price": 59.99},
#          {"Title": "Cooking Mama 2: Dinner with Friends", "Genre": "simulation", "Price": 11.00},
#          {"Title": "Overcooked! All You Can Eat", "Genre": "simulation", "Price": 24.99},
#          {"Title": "Tetris 99", "Genre": "arcade", "Price": 0.00}
# ]

"""//////////
(a) """

# print("Games worth more than USD 20.00:")
# for item in games:
#     if int(item["Price"]) > 20.00:
#         print(str(item["Title"]))

"""//////////
(b) """

# print("Simulation games worth less than USD 20.00:")
# for item in games:
#     if str(item["Genre"]) == "simulation" and int(item["Price"]) < 20.00:
#         print(str(item["Title"]))

"""Question 2
////////// """

# stack = []
# print(f'Numbers in stack: {stack}')

# while True:
#     option = int(input("Enter a number >> "))
#     if option > 0:
#         if len(stack) < 3:
#             stack.append(option)
#             print(f'Numbers in stack: {stack}')
#         else:
#             print(f'Stack is full, unable to add number {option}')
#     elif option == -1:
#         if len(stack) > 0:
#             stack.pop()
#             print(f'Numbers in stack: {stack}')
#         else:
#             print('Stack is empty, unable to pop a number')
#     elif option == 0:
#         """print(f'{option} entered, quitting program')
#                             OR"""
#         print('0 entered, quitting program')
#         break
#     else:
#         print('Enter a valid number')

"""Question 3
////////// """

# int_list = [50, -4, 7, 61, 23]

"""//////////
Part 1 """



"""//////////
Part 2 """



"""//////////
Part 3 """

# def product(list):
#     if len(list) == 1:
#         return list[0]
#     else:
#         return list[0] * product(list[1:])

# print(f'The product of all numbers in the list is {product(int_list)}')

"""//////////
Part 4 """

# def content(list):
#     if len(list) == 1:
#         return str(list[0])
#     else:
#         return str(list[0]) + str(content(list[1:]))

# print(f'{content(int_list)}')