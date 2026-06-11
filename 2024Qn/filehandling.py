with open("example.txt", "w") as f:
    f.write("1. first sentence")
    print("sentence written succssfully")

f = open("example.txt", "a")
f.write("2. Second line ")
f.write("3. Second line ")

f.close()

f = open("example.txt", "r")
print(f.read())

f.close()