"""Given an integer,n, print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary

The four values must be printed on a single line in the order specified above for each i from 1 to number . 
Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space."""

def print_formatted(number):
    # your code goes here
    x=len(f"{number:b}")
    for i in range(1,number+1):
        
        a=len(f"{i:d}")
        b=len(f"{i:o}")
        c=len(f"{i:x}")
        d=len(f"{i:b}")
        
        e=x-a
        f=x-b
        g=x-c
        h=x-d
        #print(x)
        while(e>0):
            print(" ",end='')
            e-=1
        print(f"{i:d}",end=' ')
        
        while(f>0):
            print(" ",end='')
            f-=1
        print(f"{i:o}",end=' ')
        
        while(g>0):
            print(" ",end='')
            g-=1
        print(f"{i:x}".title(),end=' ')
        
        while(h>0):
            print(" ",end='')
            h-=1
        print(f"{i:b}",end='\n')
        
if __name__ == '__main__':
    n = int(input("Enter a number:"))
    print_formatted(n)