# Write a python script to calculate sum of digits of a given number
a=input("Enter a number: ")
i=0
for b in a:
    c=int(b)
    if i==0:
        e=c
        i+=1
        continue
    e=e+c
print(e)

    
