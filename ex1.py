while True:
    text = input('Please, enter some text\n')
    if len(text) == 0:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
    else:
        #text was successfully validated!
        #we're ready to exit the loop.
        break

while True:
    try:
        num = int(input('Please, enter a number for repetition\n'))
    except ValueError:
        print("Sorry, your value is not a number")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break

result = ''

for i in range(num):
    result+=text+' '

print(result)