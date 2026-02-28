"""In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string."""

def count_substring(string, sub_string):
    size=len(string)-len(sub_string)
    count=0
    for i in range(size+1):
        if string[i:i+len(sub_string)] == sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input("Enter string:").strip()
    sub_string = input("Enter substring:").strip()
    
    count = count_substring(string, sub_string)
    print(count)