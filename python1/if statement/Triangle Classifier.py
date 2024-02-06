first_side = int(input("Enter first side: "))
second_side = int(input("Enter second side: "))
third_side = int(input("Enter third side: "))
if first_side == second_side == third_side:
    print("The triangle is equilateral.")
elif first_side == second_side or first_side == third_side or second_side == third_side:
    print("The triangle is isosceles.")
elif first_side != second_side != third_side:
    print("The triangle is scalene.")
