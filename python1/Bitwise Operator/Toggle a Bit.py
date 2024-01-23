num = int(input("Enter value of num: "))
bit_pos = int(input("Enter bit position to toggle (0-indexed): "))
mask = 1 << bit_pos
result = num ^ mask
print(f"Result: {result}")
