if __name__=="__main__":
    t=int(input())
    for i in range(t):
        try:
            a,b=map(int,input().split())
            x=1//0
            print(x)
        except ZeroDivisionError:
            print("Error Code:integer division or modulo by zero")
        except ValueError as v:
            print("Error Code:",v)