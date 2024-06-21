num=int(input('enter a number: '))
fname,sname=input('enter a fullname:').split(' ')

for i in range(1,num+1):
    if (i%3==0):
       print(fname)  
    elif (i%5==0):
       print(sname)
    else:
       print(i)   