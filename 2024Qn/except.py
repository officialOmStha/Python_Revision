try:
    print(5/2)
    10/0
except ZeroDivisionError:
    print("division by zero")

li = [1,2,3,4,5,6,7,8,9,10]

try:
    print(li[4])
    print(li[22])
except IndexError:
    print("Index out of bound")

