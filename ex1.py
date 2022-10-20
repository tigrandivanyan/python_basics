#loop for inputing and validating text
while True:
    text = input('Please, enter some text\n')
    if len(text) == 0:
        print("Sorry, I didn't understand that.")
    else:
        break

#loop for inputing and validating numer
while True:
    try:
        num = int(input('Please, enter a number for repetition\n'))
    except ValueError:
        print("Sorry, your value is not a number")
        continue
    else:
        break

result = ''
#adding texts to result as wanted
for i in range(num):
    result+=text+' '

print(result)