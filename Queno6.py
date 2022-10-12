# Write a python script to calculate factorial of a given number
a=int(input('Enter a number: '))
r=range(a,0,-1)
i=0
for x in r:
    if i==0:
        b=a
    c=x-1
    if c==0:
        break
    b=(b*c)
    i+=1
print(b)
    

