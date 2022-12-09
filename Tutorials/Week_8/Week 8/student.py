with open("Week_8/Week 8/student.txt") as file:
    for line in file:
        splitData = line.split("//")
        cgpa = ((float(splitData[2]) + float(splitData[3]) + float(splitData[4]) + float(splitData[5]))/4)
        print(f"{splitData[1]} (Student ID: {splitData[0]}) have a {cgpa} CGPA")