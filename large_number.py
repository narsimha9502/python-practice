# Find the largest among three numbers
n1 = int(input('Enter a n1 value: '))
n2 = int(input('Enter a n2 value: '))
n3 = int(input('Enter a n3 value: '))
if (n1>=n2) and (n1>=n3):
    larger=n1
elif (n2>=n1) and (n2>=n3):
    larger=n2
else:
    larger=n3
print('the largest number is',larger)            
