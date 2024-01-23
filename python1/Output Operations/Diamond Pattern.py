integer = eval(input("Enter an odd integer: "))

if integer % 2 == 1:
    for i in range(integer):
        if i < integer // 2 + 1:
            print(' ' * (integer // 2 - i) + '*' * (2 * i + 1))
        else:
            print(' ' * (i - integer // 2) + '*' * (2 * (integer - i) - 1))
else:
    print("The number is not odd. Please enter an odd number.")
