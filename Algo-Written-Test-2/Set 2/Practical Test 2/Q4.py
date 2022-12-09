student_list = [{"std_id":"035721","cgpa":"3.4"},
    {"std_id":"036013","cgpa":"2.8"},
    {"std_id":"039026","cgpa":"2.2"},
    {"std_id":"037843","cgpa":"4.0"},
    {"std_id":"031284","cgpa":"3.7"},
    {"std_id":"038032","cgpa":"1.8"}
]

print("The list of students with CGPA more than 3.0>> ")
count = 0
for element in student_list:
    if float(element["cgpa"]) > 3.0:
        count += 1
        print(count, ".", element["std_id"])