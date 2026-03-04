if __name__=="__main__":
    t=int(input())
    for i in range(t):
        try:
            a,b=map(int,input().split())
            x=a//b
            print(x)
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as v:
            print("Error Code:",v)