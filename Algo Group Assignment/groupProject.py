import sys
import time

# Student_ID // Name // Algorithm // Computing_Mathematics // English // Web_Programming
def checkID(enteredID):
    with open ("credentials.txt", "r") as file:
        ID = [line.split()[0] for line in file]
        if enteredID in ID:
            return True
        else:
            return False
    
def askToMakeNewID(ID):
    menu = input("That ID doesn't exist, would you like to register this new ID? (Y or N) ")
    if menu.upper() == "Y":
        name1 = input("Enter First name >> ")
        name2 = input("Enter surname >> ")

        name1 = name1.upper()
        name2 = name2.upper()

        with open("credentials.txt", "a") as file:
            add = ("\n" + ID + " // " + name1 + " // " + name2 + " // ungraded // ungraded // ungraded // ungraded")
            file.write(add)
            file.close()
        with open("credentials.txt", "r") as file:
            lines = file.readlines()
            for row in lines:
                value = row.split(" // ")
                if value[0] == ID:
                    user = value
                    break
            return user
    else:
        print("Invalid input...\n")
        __main__()

def UI1():
    global IDexists
    while True:
        menuUI1 = input("===================================\n\
Welcome, select an option to begin:\n\
1 --> Login with Student ID\n\
2 --> End Program\n\
===================================\n\
Enter an option >> ")
        if menuUI1 == "1":
            ID = input("\nEnter Student ID >> ")
            IDexists = checkID(ID)

            if IDexists is True:
                with open("credentials.txt", "r") as file:
                    lines = file.readlines()
                    for row in lines:
                        value = row.split(" // ")
                        if value[0] == ID:
                            user = value
                            break
                    return user, ID

            else:
                return askToMakeNewID(ID), ID

        elif menuUI1 == "2":
            endProgram()
        # user interface, checks for student ID from txt file. (name optional)
        # has a end programs option
        else:
            print("Invalid Option...\n")

def calcTotalGrade(user):
    print("Marks-->")
    displayMarks(marks)
    x = 0
    print("Grades-->")
    subjectList = ["Algorithm", "Computing Mathematics", "English", "Web Programming"]
    for grade in user[3:]:
        subject = subjectList[x]
        x += 1
        if grade == "ungraded" or grade == "ungraded\n":
            print("No Grades entered")
            continue
        grade = int(grade)
        if grade >= 80 and grade <= 100:
            print(f"\tGrade for {subject} is A")
        elif grade >= 75 and  grade < 80:
            print(f"\tGrade for {subject} is A-")
        elif grade >= 70 and grade < 75:    
            print(f"\tGrade for {subject} is B+")
        elif grade >= 65 and grade < 70:
            print(f"\tGrade for {subject} is B")
        elif grade >= 60 and grade < 65:
            print(f"\tGrade for {subject} is B-")
        elif grade >= 55 and grade < 60:
            print(f"\tGrade for {subject} is C+")
        elif grade >= 50 and grade < 55:
            print(f"\tGrade for {subject} is C")
        elif grade >= 47 and grade < 50:
            print(f"\tGrade for {subject} is D+")
        elif grade >= 44 and grade < 47:
            print(f"\tGrade for {subject} is D")
        elif grade >= 40 and grade < 44:
            print(f"\tGrade for {subject} is D-")
        elif grade >= 0 and grade < 40:
            print(f"\tGrade for {subject} is F")
        else:
            print("Error, invalid grade detected...")
    print("")

def endProgram():
    print("\nEnding program...")
    time.sleep(0.5)
    print("Ending pro..")
    time.sleep(0.5)
    print("Endi.")
    time.sleep(0.5)
    print("")
    sys.exit()

def addToFile(user, mark, option, ID):
    with open("credentials.txt", "r") as file:
        lines = file.readlines()
        count = 0
        for element in lines:
            count += 1
            data = element.split(" // ")
            if data[0] == user[0]:
                data[option + 2] = mark
                if int(mark) >= 0 and int(mark) <= 100: 
                    if option == 1 or option == 2 or option == 3:
                        new_line = (data[0] + " // " + data[1] + " // " + data[2] + " // " + data[3] + " // " + data[4] + " // " + data[5] + " // " + data[6])
                    elif option == 4 and IDexists is True:
                        new_line = (data[0] + " // " + data[1] + " // " + data[2] + " // " + data[3] + " // " + data[4] + " // " + data[5] + " // " + data[6] + "\n")
                    elif option == 4:
                        new_line = (data[0] + " // " + data[1] + " // " + data[2] + " // " + data[3] + " // " + data[4] + " // " + data[5] + " // " + data[6])
                    else:
                        continue
                    lines[count- 1] = new_line
                else:
                    print("ERROR: Enter a valid mark!")
                    continue
            else: 
                continue        

    with open("credentials.txt","w") as file:
        file.writelines(lines)
        file.close()
    with open("credentials.txt", "r") as file:
        lines = file.readlines()
        for row in lines:
            value = row.split(" // ")
            if value[0] == ID:
                user = value
                break
        return user

def calcGPA(user):
    grades = []
    x = 0
    subjectList = ["Algorithm", "Computing Mathematics", "English", "Web Programming"]
    for grade in user[3:]:
        subject = subjectList[x]
        x += 1
        if grade == "ungraded" or grade == "ungraded\n":
            continue
        grade = int(grade)
        if grade >= 80 and grade <= 100:
            print(f"GPA for {subject} is 4.00")
            gpa = "4.00"
            grades.append(float(gpa))
        elif grade >= 75 and  grade < 80:
            print(f"GPA for {subject} is 3.67")
            gpa = "3.67"
            grades.append(float(gpa))
        elif grade >= 70 and grade < 75:    
            print(f"GPA for {subject} is 3.33")
            gpa = "3.33"
            grades.append(float(gpa))
        elif grade >= 65 and grade < 70:
            print(f"GPA for {subject} is 3.00")
            gpa = "3.00"
            grades.append(float(gpa))
        elif grade >= 60 and grade < 65:
            print(f"GPA for {subject} is 2.67")
            gpa = "2.67"
            grades.append(float(gpa))
        elif grade >= 55 and grade < 60:
            print(f"GPA for {subject} is 2.33")
            gpa = "2.33"
            grades.append(float(gpa))
        elif grade >= 50 and grade < 55:
            print(f"GPA for {subject} is 2.00")
            gpa = "2.00"
            grades.append(float(gpa))
        elif grade >= 47 and grade < 50:
            print(f"GPA for {subject} is 1.67")
            gpa = "1.67"
            grades.append(float(gpa))
        elif grade >= 44 and grade < 47:
            print(f"GPA for {subject} is 1.33")
            gpa = "1.33"
            grades.append(float(gpa))
        elif grade >= 40 and grade < 44:
            print(f"GPA for {subject} is 1.00")
            gpa = "1.00"
            grades.append(float(gpa))
        elif grade >= 0 and grade < 40:
            print(f"GPA for {subject} is 0.00")
            gpa = "0.00"
            grades.append(float(gpa))
        else:
            print("Error, invalid grade detected...")
    
    return grades

def calcCGPA(gpa_list):
    if len(gpa_list) == 0:
        print("All subjects has not been graded...\n")
    else:
        cgpa = sum(gpa_list) / len(gpa_list)
        if cgpa == 0:
            print("Error: No grades are entered")
            UI2()
        elif cgpa < 2.00 :
            print("===================\nYour CGPA is" , round(cgpa,2),"\n===================")
        else:
            print("===================\nYour CGPA is" , round(cgpa,2),"\n===================")
 
def displayMarks(marks):
    for line in marks:
        print(f"""\t{line} : {marks[line]}""")

def UI2():    
    print("""Select an option:
    1 --> Enter marks for Algorithm
    2 --> Enter marks for Computing Mathematics
    3 --> Enter marks for English 
    4 --> Enter marks for Web Programming
    5 --> Display marks and grades
    6 --> Display GPA and CGPA
    7 --> Log out
    8 --> End the program
    """)
option = 0
marks = {
    "Algorithm" : "ungraded",
    "Computing_Mathematics" : "ungraded",
    "English" : "ungraded",
    "Web_Programming" : "ungraded"
}

def __main__():
    global option
    global marks
    user, ID = UI1()

    while True:

        UI2()
        marks["Algorithm"] = user[3]
        marks["Computing_Mathematics"] = user[4]
        marks["English"] = user[5]
        marks["Web_Programming"] = user[6]
        option = int(input("\nEnter your option >> "))

        if option == 1 or option == 2 or option == 3 or option == 4:
            mark = input("\nEnter your mark here => ")
            user = addToFile(user, mark, option, ID)
        elif option == 5:
            calcTotalGrade(user)
        elif option == 6:
            gpa_list = calcGPA(user)
            calcCGPA(gpa_list)
        elif option == 7:
            __main__()
        elif option == 8:
            endProgram()
        else:
            print("Invalid Option...\n")
            UI2()

__main__()