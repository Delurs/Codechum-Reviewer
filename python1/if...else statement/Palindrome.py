str = input("Enter a string: ")
reversed_str = str[::-1]
if str == reversed_str:
    print(f"{str} is a palindrome.")
else:
    print(f"{str} is not a palindrome.")
