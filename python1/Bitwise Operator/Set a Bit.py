value = int(input("Enter value: "))
bit_pos = int(input("Enter bit position: "))
mask = 1 << bit_pos
result = value | mask
print(f"The new value is: {result}")
