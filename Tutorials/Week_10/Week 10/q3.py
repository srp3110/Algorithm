def sum(data):
    total = 0
    for element in data:
        if type(element) == type([]):
            total = total + sum(element)
        else:
            total = total + element
    return total

data = [[1,2], [3,4], [5,6]]
print(sum(data))