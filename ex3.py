#loop for inputing and validating numer
while True:
    numText = input('Please, enter a number for calculating sum of digits\n')
    if not numText.isnumeric():
        print("Sorry, your value is not a number")
        continue
    else:
        break

sum = 0
#calculating the sum by converting each char to int
for character in numText:
    sum += int(character)

print(sum)