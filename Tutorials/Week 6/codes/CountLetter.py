word = input("Enter a word >> ")
letter = input("Enter a letter to count >> ")
word = word.lower()
letter = letter.lower()
qty = 0
for same_letter in word:
    if same_letter == letter:
        qty += 1
print(f"Quantity of letter {letter} is {qty}")