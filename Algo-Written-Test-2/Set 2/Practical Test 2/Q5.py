data = [-2, 1, 1, 3, 3, 3, 4, 5, 6, 78, 78, 79]
new_data = []

def remove_duplicates(data):
    for num in data:
        if num not in new_data:
            new_data.append(num)


    return new_data 

print(remove_duplicates(data))



