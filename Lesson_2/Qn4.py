# nested if to find if a person is child, teen, adult or senior.

age = int(input("Enter your age: "))

if age >= 0:
    if age <= 12:
        print("Child")
    else:
        if age <= 17:
            print("Teenager")
        else:
            if age <= 56:
                print("Adult")
            else:
                print("Senior Citizen")

else:
    print("Invalid Input")