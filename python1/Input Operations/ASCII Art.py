import string

characters = string.ascii_letters + string.digits

char = input("Enter a character: ")

if char not in characters:
    print("Invalid input.")
else:
    print(f"""*****
*   *
* {char} *
*   *
*****""")
