# Write a python script to calculate sum of first N even natural numbers
a=int(input("Enter a Number: "))
b=0
i=1
while i<=a:
    if i%2==0:
        b=(i+b)
    i+=1    
print(b)
    