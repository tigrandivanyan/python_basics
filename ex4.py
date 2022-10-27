# function for making a string from list
def listToString(arr):
 
    str1 = ""
 
    for elem in arr:
        if arr[len(arr) - 1] != elem:
            str1 += elem + "-"
        else:
            str1 += elem
 
    return str1

#loop for inputing and validating text
while True:
    text = input('Please, enter some text with 2 or more characters and at least 1 space\n')
    if len(text) == 0:
        print("Sorry, I didn't understand that.")
    elif len(text) < 3:
        print("Sorry, the length of text should be 2 or more")
    else:
        break

arr = text.split(" ")
if len(arr) == 1:
    print('Sorry your text does not contain any spaces')
else:
    print(listToString(arr))