#loop for inputing and validating numer
while True:
    try:
        num = int(input('Please, enter a number for displaying prime numbers before it\n'))
    except ValueError:
        print("Sorry, your value is not a number")
        continue
    else:
        break

print("Here you go:")
for numik in range(2, num+1):
    prime = True
    for i in range(2, numik):
        if (numik % i == 0):
            prime = False
    if prime:
       print (numik)