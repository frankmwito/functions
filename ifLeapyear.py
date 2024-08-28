def leap_year():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

result = leap_year()
if result:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")
