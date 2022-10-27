#loop for inputing and validating text
while True:
    text = input('Please, enter some text with 3 or more characters\n')
    if len(text) == 0:
        print("Sorry, I didn't understand that.")
    elif len(text) < 3:
        print("Sorry, the length of text should be 3 or more")
    else:
        break

#swapcasing every 3rd character by recreating string
res = ''
for idx, ele in enumerate(text):
 
    if (idx + 1) % 3 == 0 and idx != 0:
        res = res + ele.swapcase()
    else:
        res = res + ele
print(res)
