"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above.
 Iterate through each command in order and perform the corresponding operation on your list."""

if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(N):
        command,*num=input().split()
        number=list(map(int,num))
        if command.lower()=="insert":
            L.insert(number[0],number[1])
        elif command.lower()=="print":
            print(L)
        elif command.lower()=="remove":
            L.remove(number[0])
        elif command.lower()=="append":
            L.append(number[0])
        elif command.lower()=="sort":
            L.sort()
        elif command.lower()=="pop":
            L.pop()
        else:
            L.reverse()