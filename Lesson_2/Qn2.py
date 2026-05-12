# Stuent passed or failed.
mark = float(input("Enter your marks: "))
if mark >= 40 and mark <= 100:
    print("Passed")
elif mark < 40 and  mark > 0:
    print("Failed")
else:
    print("Invalid input.")