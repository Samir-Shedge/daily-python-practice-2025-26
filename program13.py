# Write a Python Program to Check Leap Year.

# import calendar

year = int(input("Please enter valid year (four digits): "))

# print(calendar.isleap(year))
# if calendar.isleap(year) == True:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a Leap year")
    

