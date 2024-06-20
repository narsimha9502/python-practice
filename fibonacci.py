'''num=int(input('enter a number:'))
a=0
b=1
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c)'''
num = int(input('enter a number: '))
n1,n2=0,1
if num <=0:
    print('enetr positive number..')
elif num ==1:
    print('fibonacci sequece is',num)
else:
    print('fibonacci sequence:')
    for i in range(2,num):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)
    


