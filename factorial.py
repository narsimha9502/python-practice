#find the factorial number
num =int(input('Enter a number: '))
if (num<0):
    print('invalid number.')
elif (num==0):
    print('factorial of 0 is 1.')
else:
    fac=1
    for i in range(1,num+1):
        fac=fac*i
print('factorial of {} is {}'.format(num,fac))        


'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
number=int(input('enter a number:'))
print(f'the factorial of {number} is {factorial(number)}') '''   