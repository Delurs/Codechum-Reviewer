import sys

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))
try:
    quotient = dividend / divisor
except ZeroDivisionError:
    print("Error: divisor cannot be zero")
    sys.exit()
print(f"Quotient = {int(quotient)}")
