# function to add any numbers passed as parameters.

def add(x,y, *args):
    return x + y + sum(args)

print(f"The sum of 10, 20, 30 is {add(10,20,30)}")