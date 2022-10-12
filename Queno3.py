# Write a python script to calculate sum of cubes of first N natural numbers
a=int(input('Enter a Number: '))
b=0
i=1
while i<=a:
    b=(b+i)
    i+=1
print(b**3)    