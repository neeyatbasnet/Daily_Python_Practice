import textwrap

def wrap(string, max_width):
    strg=textwrap.fill(string,max_width)
    return strg

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)