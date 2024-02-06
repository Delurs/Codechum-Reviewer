letter = input("Enter a letter: ")
if letter.upper() in ["A", "E", "I", "O", "U"]:
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")
