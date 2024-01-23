num = int(input("Enter a number: "))

multiply = {}

for i in range(1,11):
    multiply[i] = num*i

for i in range(1,11):
    print(f"{num} x {i} = {multiply[i]}")
