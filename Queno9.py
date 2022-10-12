# Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
from audioop import reverse


a=input('Enter a number: ')
b=int(a)
string=""
while b>0:
      d=b%2
      b=b//2
      string=str(d)+string
print(string)
          
          
      
  

        



