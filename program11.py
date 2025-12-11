# Write a Python Program to Check if a Number is Positive, Negative or Zero.

number = float(input("Enter a number: "))

if number < 0:
    print(f"{number} is negative number.")
elif number > 0:
    print(f"{number} is positive number.")
else:
    print("number is zero.")