# Check Prime

uip = int(input("Enter a number: "))

prime = True

for i in range(2,uip):
    if uip < 2:
        prime = False
        break
    if uip % i == 0:
        prime = False
        break

if prime:
    print(f"{uip} is a prime number.")
else:
    print(f"{uip} is not a prime number.")

