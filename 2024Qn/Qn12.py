# Program to count no of vowel in string

vowel = 'aeiouAEIOU'
ui = input("Enter a string: ")
vcount = 0

for i in range(len(ui)):
    if ui[i] in vowel:
        vcount += 1

print(f"There is {vcount} vowel characters.")