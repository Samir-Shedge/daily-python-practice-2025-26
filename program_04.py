# Write a Python program to swap two variables.


# Method 1 - using simple python tuple
a = 10
b = 5
print(f"before swapping - value of a is {a} and b is {b}")

a, b = b, a
print(f"after swapping - value of a  is {a} and b is {b}")


# Method 2 - using temporary vsriable
x = 3
y = 6
print(f"before swapping - value of a is {x} and b is {y}")

temp = x
x = y
y = temp
print(f"after swapping - value of a  is {x} and b is {y}")
print(temp)



