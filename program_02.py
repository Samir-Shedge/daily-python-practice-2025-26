# Write a python program to do arithmetic operations addition and division

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
result = num1 + num2
print(f"The addition of {num1} and {num2} is: {result}")

num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))


if num4 == 0:
    print("Cannot divide by zero")
else:
    result = num3/num4
    print(f"The division of {num3} and {num4} is: {result}")


# try:
#     num4 == 0
# except ZeroDivisionError as e:
#     print(e)
# print(num3 / num4)
