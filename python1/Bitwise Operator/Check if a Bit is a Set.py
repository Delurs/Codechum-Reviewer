num = int(input("Enter an integer: "))
bit = int(input("Enter the bit position: "))
mask = 1 << bit
result = ACnum & mask
if result != 0:
    print("Yes")
else:
    print("No")
