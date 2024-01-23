year = int(input("Enter a year: "))
# divide the year by 4 to check if its a leap year
if year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
