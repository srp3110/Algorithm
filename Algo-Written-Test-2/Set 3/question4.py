employee_list = [{"employee_name":"Sarah","salary":"28000"},
                {"employee_name":"Jonathan","salary":"80000"},
                {"employee_name":"Dylan","salary":"57000"},
                {"employee_name":"Benjamin","salary":"32000"},
                {"employee_name":"Alice","salary":"20000"},
                {"employee_name":"Rosa","salary":"89000"}
                ]
employee = []
x = 0
for lines in employee_list:
    if int(lines["salary"]) > 50000:
        employee.append(lines["employee_name"])
print("The list of employees with salary more than 50,000 >>")
for name in employee:
    x += 1
    print(f"{x}. {name}")
