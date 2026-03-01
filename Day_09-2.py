def solve(s):
    result = ""
    prev_space = True
    
    for ch in s:
        if ch.isalpha() and prev_space:
            result += ch.upper()
        else:
            result += ch.lower()
        
        prev_space = ch.isspace()
    
    return result

if __name__ == '__main__':
    s = input("Enter a string:")
    result = solve(s)
    print(result)
