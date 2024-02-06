age = int(input("Enter your age: "))
if age == 0:
    print("You belong to the infant age category.")
if age <= 3:
    print("You belong to the toddler age category.")
if 5 <= age <= 12:
    print("You belong to the school age category.")
if 13 <= age <= 18:
    print("You belong to the teenager age category.")
if 19 <= age <= 65:
    print("You belong to the adult age category.")
if age >= 66:
    print("You belong to the senior age category.")
