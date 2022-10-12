# Write a python script to calculate sum of squares of first N natural numbers
a=int(input('Enter a number: '))
b=0
i=1
while i<=a:
    b=(i+b)
    i+=1
print(b**2)    