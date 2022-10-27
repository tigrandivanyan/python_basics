#loop for inputing and validating numer
while True:
    try:
        n = int(input("Enter the number 'N' : "))
    except ValueError:
        print("Sorry, your value is not a number")
        continue
    else:
        break
# first two terms
n1, n2 = 0, 1
count = 0
arr = []
# check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto",n,":")
    arr.append(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while n1 < n:
        arr.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
print(arr)