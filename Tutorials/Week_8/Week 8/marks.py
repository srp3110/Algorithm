totalA = 0
totalB = 0
totalC = 0
countA = 0
countB = 0
countC = 0

with open("Week_8/Week 8/marks.txt") as file:
    content = file.read().split()
    print(content)
    
    for i in range(0, len(content), 2):
        if content[i+1] == "A":
            totalA += int(content[i])
            countA += 1
        elif content[i+1] == "B":
            totalB += int(content[i])
            countB += 1
        elif content[i+1] == "C":
            totalC += int(content[i])
            countC += 1

print(f'''
Average mark for A is {round(totalA/countA, 2)}
Average mark for B is {round(totalB/countB, 2)}
Average mark for C is {round(totalC/countC, 2)}
''')