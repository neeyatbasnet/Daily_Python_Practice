"""Write a function to take an immutable string and modify a char on the specified index i and then print the modified string"""

def mutate_string(string, position, character):
    strg=string [:position]+character+string[position+1:]
    return strg

if __name__ == '__main__':
    s = input()
    try:
        i, c = input().split()
        s_new = mutate_string(s, int(i), c)
        print(s_new)
    except:
        print("Second input should specify index and charcter to be put separated by a space")
    