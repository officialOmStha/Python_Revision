# While Loop
x = 1

while x < 11:
    print(x)
    x += 1


# To print even numbers.
for i in range(1,101):
    if i % 2 == 0:
        print(i)


# factorial using loop.

fac = 1
n = 5
for i in range(1,n+1):
    fac *= i
print("Factorial of",n, "is",fac)
