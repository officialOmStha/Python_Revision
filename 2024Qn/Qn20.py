class Dog:
    def sound(self):
        print("Woff Woff")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog's name is {self.name}"
class Chiwawa(Dog):
    def sound(self):
        print("Hawu Hawuu")

obj_dog = Dog("Kali")

obj_dog.sound()
print(obj_dog)

obj_chiwa = Chiwawa("Puntay")
obj_chiwa.sound()
print(obj_chiwa)
