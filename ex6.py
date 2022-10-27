arr = []

#loop for inputing and validating numer
while True:
    try:
        n = int(input("Enter number of elements : "))
    except ValueError:
        print("Sorry, your value is not a number")
        continue
    else:
        break

print('Now enter each element and press eneter')
# iterating till the range
for i in range(0, n):
    ele = input()
  
    arr.append(ele) # adding the element

temp = []

#removing unnecesarry elements
for elem in arr:
    if elem not in temp:
        temp.append(elem)

arr = temp

print(f'Updated List after removing duplicates = {temp}')

    

