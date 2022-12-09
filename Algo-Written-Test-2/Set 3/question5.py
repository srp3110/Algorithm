print("Type in the GPA for each semester or \"done\" to finish")
option = 0
semester = 0
count = 0
listGPA = []
totalGPA = 0
aboveAverage = 0
while option != "done":
    semester += 1
    option = input(f"Semester {semester} GPA: ")
    if option == "done":
        break
    listGPA.append(float(option))
for values in listGPA:
    totalGPA += values
    count += 1
averageGPA = round(totalGPA / count, 2)
for values in listGPA:
    if values > averageGPA:
        aboveAverage += 1
print("Average GPA =", averageGPA)
print(aboveAverage,"semester were above average")