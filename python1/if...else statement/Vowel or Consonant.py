letter = input("Enter a letter: ")
if letter.lower() not in {"a", "e", "i", "o", "u"}:
    print(f"{letter} is a consonant.")
else:
    print(f"{letter} is a vowel.")
