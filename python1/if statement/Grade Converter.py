grade = int(input("Enter percentage grade: "))
if grade >= 90: 
    print("Letter grade: A")
if 80 <= grade <= 89:
    print("Letter grade: B")
if 70 <= grade <= 79:
    print("Letter grade: C")
if 60 <= grade <= 69:
    print("Letter grade: D")
if grade < 59:
    print("Letter grade: F")
