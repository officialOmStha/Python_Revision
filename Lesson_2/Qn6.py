# Multiplication table.

m = int(input("Enter the number for multiplication table: "))

for i in range(1,11):
    print(f"{m} * {i} = {m * i}")

# To count vowel in a string
sentence = "lets go on a play date."
vow = ["a", "e", "i", "o", "u"]

count = 0
for a in range(0,len(sentence)):
    if sentence[a] in vow:
        count += 1

print(f"There are {count} vowel letters.")

# For with else clause

tf ="Hello"
for x in range(1,5):
    if tf[x] == "z":
        print("Found")
else:
    print("Not found")


# demonstration of pass, continue, break:
for j in range (10):
    if j == 0:
        pass
    if j == 1:
        continue
    if j == 7: 
        break
    print(j)
