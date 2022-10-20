#loop for inputing and validating text
while True:
    text = input('Please, enter some text with 3 or more characters\n')
    if len(text) == 0:
        print("Sorry, I didn't understand that.")
    elif len(text) < 3:
        print("Sorry, the length of text should be 3 or more")
    else:
        break
#swapcasing 3rd character by recreating string
text = text[:2] + text[2].swapcase() + text[3:]
print(text)
