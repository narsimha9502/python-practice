#To solve qudratic equtaion
import cmath
a=int(input('enter a number:'))
b=int(input('enter a number:'))
c=int(input('enter a number:'))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print(f'The qudratic solution are {sol1} and {sol2}')
