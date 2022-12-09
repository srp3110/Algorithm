try:
    with open("data.txt") as file:
        value = file.read()
except:
    print("File not found")