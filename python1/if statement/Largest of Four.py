num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
largest = num1
if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

if num4 > largest:
    largest = num4

print(f"The largest number is {largest}")
