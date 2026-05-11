# program to swap the values
a = 5
b = 10
print(f"a = {a}, b = {b}")

temp = a
a = b 
b = temp 
print(f"a = {a}, b = {b}")

# without temp variable:
x = 5
y = 10
print(f"x = {x}, y = {y}")

x = x + y
y = x - y 
x = x - y
print(f"x = {x}, y = {y}")



