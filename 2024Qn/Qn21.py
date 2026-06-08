class Rectangle:
    def __init__(self, length : float, breadth : float):
        self.length = length
        self.breadth = breadth

    def area(self):
        tot_are = self.length * self.breadth
        return f"The area of rectangle is {tot_are}"
    
    def perimeter(self):
        tot_peri = 2 *(self.length + self.breadth)
        return f"The perimeter of rectangle is {tot_peri}"
    
obj1 = Rectangle(7, 3)
print(obj1.area())
print(obj1.perimeter())

obj2 = Rectangle(8, 4)
print(obj2.area())
print(obj2.perimeter())
