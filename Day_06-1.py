"""You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa."""

def swap_case(s):
    L=list(s)
    for i in range(len(L)):
        if L[i].isupper():
            L[i]=L[i].lower()
        else:
            L[i]=L[i].upper()
    
    s="".join(L)        
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)