list_num = [90, 34, 67, 12, 59]

def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])

print(sum(list_num))