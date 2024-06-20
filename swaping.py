#swaping values
x = int(input('Enter a value of x: '))
y = int(input('Enter avalue of y: '))
temp=x
x=y
y=temp
print(f'The value of x after swaping:',x)
print(f'The value of y after swaping:',y)
#another method
x = int(input('Enter a value of x: '))
y = int(input('Enter avalue of y: '))
x,y=y,x
print(f'The value of x after swaping:',x)
print(f'The value of y after swaping:',y)