"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up."""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst=list(arr)
    max=-100
    max1=-100
    for i in lst:
        if max<i:
            max=i
    lst=[x for x in lst if x!=max]
    for i in lst:
        if max1<i:
            max1=i
    print(max1)
    
    