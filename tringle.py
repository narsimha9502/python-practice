#Calculate the area of tringle
a = float(input('Enter a first side: '))
b = float(input('Enter a second side: '))
c = float(input('Enter a third side: '))
#calcuate semi-perimeter
s=(a+b+c)/2
#calculate the area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(f'The area of triangle is {area}')