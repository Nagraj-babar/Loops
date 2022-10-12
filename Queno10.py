# Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
a=input("Enter a number: ")
b=int(a)
d=""
while b>=1:
    c=b%8
    b=b//8
    d=str(c)+d
print(d)

    